"""Lightweight documentation checks; not an application or JSON Schema validator."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
count = 0
for path in root.rglob("*.md"):
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text()):
        if "://" in target or target.startswith("#"):
            continue
        assert (path.parent / target.split("#")[0]).exists(), (path, target)
    count += 1
schema = json.loads((root / "schemas/venue.schema.json").read_text())
assert schema["type"] == "object" and "venue_id" in schema["required"]
manifest = json.loads((root / "data-source-manifest.json").read_text())
assert manifest["snapshot"]["venue_count"] == 1118
assert len(manifest["snapshot"]["sha256"]) == 64
assert not (root / "data/dataset.json").exists(), "Private dataset unexpectedly inside repo"
print(f"PASS: {count} Markdown documents, local links, schema JSON, source manifest")
