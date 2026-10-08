"""Build the preview from local data without adding restaurant content to Git."""

import argparse
import hashlib
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()

project_root = Path(__file__).resolve().parents[1]
selection = json.loads(
    (project_root / 'prototypes/pilot-selection.json').read_text()
)
dataset = json.loads(args.dataset.read_text())
venues_by_id = {venue['venue_id']: venue for venue in dataset['venues']}

preview_venues = []
review_records = []

for item in selection['records']:
    venue = venues_by_id[item['venue_id']]
    assert venue['city_id'] == 'tr-istanbul'

    source_url = venue['source_records'][0]['listing_url']
    review_records.append({
        **item,
        'name': venue['name'],
        'address': venue['address']['raw'],
        'research_status': 'not_started',
        'source': source_url,
    })

    if item['include_in_preview']:
        instagram = next((
            account for account in venue.get('social_accounts', [])
            if account.get('platform', '').lower() == 'instagram'
            and account.get('verification_status') == 'verified'
        ), None)
        videos = [
            video for video in venue.get('videos', [])
            if video.get('platform', '').lower() == 'youtube'
            and video.get('verification_status') == 'verified'
            and video.get('rights_status') in ['owned', 'licensed', 'permission_granted']
        ]
        preview_venues.append({
            'id': venue['venue_id'],
            'name': venue['name'],
            'address': venue['address']['raw'],
            'source': source_url,
            'instagram': {'url': instagram['url']} if instagram else None,
            'videos': [
                {key: video.get(key) for key in ['url', 'title', 'attribution']}
                for video in videos
            ],
        })

template = (project_root / 'prototypes/index.template.html').read_text()

# Source text must not be able to close the HTML script element.
preview_json = json.dumps(preview_venues, ensure_ascii=False).replace('<', '\\u003c')
preview_html = template.replace('__VENUES__', preview_json)

args.output.mkdir(parents=True, exist_ok=True)
(args.output / 'index.html').write_text(preview_html)

review = {
    'source_sha256': hashlib.sha256(args.dataset.read_bytes()).hexdigest(),
    'selection_note': selection['selection_note'],
    'records': review_records,
}
(args.output / 'pilot-review.json').write_text(
    json.dumps(review, ensure_ascii=False, indent=2) + '\n'
)

for output_file in args.output.iterdir():
    if output_file.is_file():
        output_file.chmod(0o600)
args.output.chmod(0o700)

print(
    f'Built {len(preview_venues)} preview venues; '
    f'{len(review_records)} pilot review records'
)
