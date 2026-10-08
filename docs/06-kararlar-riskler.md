# Kararlar, açık sorular ve riskler

## Karar kayıtları

| ID | Konu | Durum | Kayıt |
|---|---|---|---|
| K-001 | Ürün değeri | Kullanıcı yönü belli | Yerel yemek keşfi, karar desteği, güçlü UI/UX |
| K-002 | Veri korunması | Yapıldı | Tüm mevcut şehir kaynakları ve ortak veri seti yerelde |
| K-003 | İlk şehir/hedef kişi | Prototip çalışma varsayımı | “Devam et” sonrası İstanbul’da yaşayan günlük karar vericiyle ilerleniyor; nihai kapsam kararı değil |
| K-004 | Üyelik/favori/rota | Prototip çalışma varsayımı | Üyeliksiz keşif; rota sonraya. Karşılaştırma UX denemesi, kalıcı favori yok |
| K-005 | Repo hesabı/adı/görünürlüğü | Oluşturuldu | alphanAkbulut/gastronomi-duraklari, private; ilk commit/push açık onay bekliyor |
| K-006 | Bütçe ve teknoloji | Yanıt bekliyor | Henüz sağlayıcı, ücret veya yığın seçilmedi |
| K-007 | Görsel yön | Açık | Referanslar ve iki yön üzerinden seçim |
| K-008 | İçerik emeği ve medya erişimi | Açık | Editör sorumluluğu ve pilot araştırma süresi gerekli |
| K-009 | Yayın/portföy | İleride karar | Public demo ile private kaynak arşivi ayrı |
| K-010 | Yönetim paneli | Kullanıcı talebi, MVP’ye alındı | Kayıt düzenleme, fotoğraf yükleme, taslak/önizleme/yayın |
| K-011 | Mekân etiketleri | Kullanıcı talebi, MVP’ye alındı | Ortak sözlükten çoklu atama, kaynak ve kontrol tarihi |
| K-012 | Ek keşif özellikleri | Önceliklendirilmiş öneri | Yemekten mekâna MVP; seçkiler/bildirim/kaydetme beta sonrası |
| K-013 | Ziyaretçi popülerliği | Kanıt bekliyor | İngilizce menü ayrı olgu; yabancı ziyaretçi tercihi dilden çıkarılmaz |

## İlk sorular

1. İlk kullanıcı ve şehir: İstanbul’da yaşayanlar mı, ziyaretçiler mi, çok şehir mi?
2. İlk sürümde üyelik ve favori gerekiyor mu? Rota sonraya kalabilir mi?
3. Repo private olarak açıldı; aylık servis bütçesi ve teknoloji tercihi hâlâ açık.

Bu cevaplardan sonra tasarım için kısa ikinci tur: sevilen/sevilmeyen örnekler, Türkçe/çok dil ihtiyacı, editoryal işi kimin yapacağı, haftalık ayrılacak süre ve hedef tanıtım tarihi. Yönetici girişi artık açık gereksinim; ziyaretçi üyeliği ayrı karar. Sağlayıcı ve ücretli servis seçimi bütçe netleşince yapılır.

## Riskler ve karşılıkları

| Risk | Etki | Yaklaşım | Sorumluluk |
|---|---|---|---|
| Çok mekân, az doğrulanmış içerik | Etkileyici görünen ama karar verdir(e)meyen katalog | Pilotla içerik eşiklerini ve gerçek süreyi öğren | Ürün sahibi + içerik sorumlusu |
| Yanlış şube/harita eşleşmesi | Kullanıcı yanlış yere gider | İsimden fazlasıyla eşleştir; çelişkiyi yayından çıkar | İçerik sorumlusu |
| Fotoğraf/video erişimi ve kullanım kısıtları | Medya eksik veya gösterilemez | Kaynak/izin kontrolü, eksik içerik tasarımı | İçerik + geliştirme |
| Genelleşmiş şablon görünümü | Ürün farkı kaybolur | Gerçek içerikle iki yön; kullanıcı göreviyle test | Tasarım + ürün sahibi |
| Üyelik/rota/yorum kapsamı büyür | Gecikme ve bakım yükü | Kapsam değişikliğini ayrı karar ve iş yap | Ürün sahibi |
| Özel veri repoya/siteye sızar | Gizlilik kaybı | Repo dışı veri, ignore kuralları, açık alan listesi, yayın kontrolü | Geliştirme |
| Sağlayıcı maliyeti/kotası belirsiz | Bütçe aşımı veya hizmet kaybı | Onaylı bütçe ve kullanım sınırı olmadan entegrasyonu açma | Ürün sahibi + geliştirme |
| Etiketin dayanağı belirsiz | Yanıltıcı tercih/popülerlik iddiası | Etiket türüne göre kanıt; tarihsiz/şüpheli atamayı yayımlamama | İçerik sorumlusu |
| Taslağın veya özel fotoğrafın sızması | Gizlilik ve yanlış yayın | Sunucu yetkisi, özel depolama, yayınlanabilir alan listesi | Geliştirme |
| Aynı cihazdaki kopyalara güvenmek | Cihaz kaybında arşiv kaybı | Bağımsız özel yedek ve geri yükleme testi | Ürün sahibi |

## Teknik karar kaydı biçimi

Başlık/ID, durum (öneri/kabul/reddedildi/değiştirildi), bağlam, gereksinim, seçenekler, seçimin gerekçesi, sonuçlar, maliyet ve geri dönüş yolu. Tarih ve kararı veren kişi eklenir. Sonradan değişen kararın önceki gerekçesi silinmez.
