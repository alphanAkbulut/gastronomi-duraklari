# Gastronomi Durakları

“Bugün nereye gitsek, ne yesek?” sorusuyla başlayan bir proje.

Bir mekân seçerken harita yorumları, Instagram hesapları ve videolar arasında dolaşıyoruz. Yine de masaya oturana kadar neyle karşılaşacağımızdan emin olamıyoruz. Gastronomi Durakları, karar vermeye yarayan bilgileri aynı yerde toplamak için doğdu: burada ne yenir, neden gidilir, hangi beklentiyle gidilir?

Başlangıç noktamız yerel lezzetler. Bir yerin pahalı, ünlü veya ödüllü olması şart değil. İyi bir öğün için onu tercih etmeye değer bir neden bulabilmek önemli.

## Şu an neredeyiz?

İlk tıklanabilir prototip hazır. Aynı içerikle iki görsel yönü deniyoruz: **Sofra Defteri** ve **Mahalle Panosu**. İsim veya adreste arama, bölge seçimi, mekân detayı ve iki adayı yan yana inceleme çalışıyor.

İlk denemeyi İstanbul’da günlük yemek kararı veren biri için, üyelik gerektirmeden hazırladık. Bu, tasarımı somutlaştırmak için seçtiğimiz başlangıç; kapsamı prototipten öğrendiklerimize göre gözden geçireceğiz. Üretim uygulamasının teknolojisi ve yayın tarihi henüz belli değil.

Mekânları düzenleyebileceğimiz, fotoğraf yükleyip etiket ekleyebileceğimiz bir yönetim paneli de MVP’ye alındı. Panelin akışını ve iş kurallarını hazırladık; henüz panel kodu veya veritabanı kurulmadı. Ziyaretçi üyeliği gerekmese de yönetici girişi olacak.

## Elimizdeki veri

8 Ekim 2026’da alınan Kültür Yolu Festivali seçkisinde 21 şehirden 1.118 mekân var. İstanbul listesi 235 kayıt içeriyor. Ad ve ham adresleri koruduk; güncel işletme durumunu, puanları ve medya kullanım haklarını henüz doğrulamadık. 29 kayıtta harita bağlantısı eksik. Kaynak kartlarında ayrı mekân detay sayfası bulunmuyor.

İlk çalışma için 20 kayıt ayırdık. 16’sı prototipte; çelişki veya eşleşme sorusu olan dört kayıt inceleme listesinde. Bu seçim bir restoran sıralaması değil. Henüz bilmediğimiz yemek önerilerini, puanları ve fotoğrafları boş bırakıyoruz.

Kaynak arşivi ve gerçek veri repo dışında, aynı ana klasörde duruyor:

```text
gastronomiDuraklari/
  lezzet_arsivi_2026-10-08/
  lezzet_dataset_v1/
  proje/
```

`schemas/venue.schema.json` ortak kayıt yapısını anlatıyor. `data-source-manifest.json` ise hangi veri kopyasıyla başladığımızı kontrol etmek için dosya özetini tutuyor. Repo tek başına restoran verisini içermiyor.

## Prototipi açmak

Yerel veri seti yukarıdaki konumdaysa repo klasöründe şu komutu çalıştır:

```sh
python3 scripts/build_prototype.py --dataset ../lezzet_dataset_v1/dataset.json --output private/ux-v1
```

Ardından `private/ux-v1/index.html` dosyasını tarayıcıda açabilirsin. Mevcut ilk çıktıyı korumak istiyorsan yeni üretimde `--output private/ux-v2` kullan. Son detay ekranı ikinci sürümdedir. Sayfanın üstünden iki tasarım arasında geçiş yapılıyor. Gerçek kayıtları içeren bu çıktı Git tarafından izlenmiyor.

Yerel sunucu kullanacaksan yalnız `private/ux-v1` klasörünü, `127.0.0.1` üzerinden aç. Böylece kaynak arşivini ve repo dosyalarını sunucuya dahil etmemiş olursun.

## Projenin notları

| Belge | İçinde ne var? |
|---|---|
| [Ürün kapsamı](docs/01-urun-kapsami.md) | Hangi sorunu çözmek istiyoruz, ilk sürüme ne giriyor? |
| [UX planı](docs/02-ux-plani.md) | Akışı ve görsel yönü nasıl deneyeceğiz? |
| [Sistem tasarımı](docs/03-sistem-tasarimi.md) | Önerilen yapı ve henüz vermediğimiz teknik kararlar |
| [Veri ve içerik](docs/04-veri-icerik.md) | Bir mekânı araştırmadan yayımlamaya kadar yapılacaklar |
| [İş planı](docs/05-teslim-plani.md) | Aşamalar, sıradaki işler ve bitirme ölçütleri |
| [Kararlar ve riskler](docs/06-kararlar-riskler.md) | Neyi biliyoruz, nerede seçim yapmamız gerekiyor? |
| [Kalite ve portföy](docs/07-kalite-portfoy.md) | Kontroller, yayın hazırlığı ve vaka çalışması |
| [İlk prototipin notları](docs/08-ilk-iterasyon.md) | Ne hazırladık, neyi denedik, ne eksik kaldı? |
| [Benzer ürünler](docs/09-benzer-urunler.md) | Hangi özellikleri inceledik, hangilerini plana aldık? |
| [Yönetim paneli](docs/10-yonetim-paneli.md) | Mekân, fotoğraf ve yayınları nasıl yöneteceğiz? |
| [Etiketler](docs/11-etiketler.md) | Etiket sözlüğü, kanıt ve filtre kuralları |
| [Mekân detayındaki içerikler](docs/12-mekan-detayi.md) | Instagram, YouTube, Google bilgileri: hazır alanlar ve kalan entegrasyon |
| [AI analiz promptu](docs/13-ai-analiz-promptu.md) | Konuşmanın ürün özeti, mevcut durum ve başka bir araçla analiz için aktarım metni |

## Nasıl çalışıyoruz?

Küçük bir işi tanımlayıp görünür bir sonuç üretmek, ardından gerçekten deneyerek ilerlemek istiyoruz. İşleri issue ile takip etmek ve kod değişikliklerini ayrı dallarda incelemek planın parçası. Henüz yapılmamış araştırmalar ve testler kendi notlarında açıkça belirtiliyor.

Doküman bağlantıları ve temel dosya kontrolleri için:

```sh
python3 scripts/check_project.py
```

[GitHub reposu](https://github.com/alphanAkbulut/gastronomi-duraklari) private olarak açıldı. Repo kodu ve proje belgelerini içerir; gerçek restoran arşivi ve üretilen özel önizlemeler repo dışında tutulur. Yazılım lisansı henüz seçilmedi.
