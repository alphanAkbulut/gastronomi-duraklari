# Proje ve teslim planı

## Yönetim yaklaşımı

Küçük, incelenebilir teslimler; her aşamada somut çıktı ve geçiş ölçütü. Ürün sahibi kapsam, tasarım ve yayın kararlarından sorumlu. Geliştirme desteği doküman, prototip, kod ve doğrulama üretir. Veri doğrulama/editörlük işini kimin yapacağı ve haftalık kapasite açık karardır; plan personel atanmış varsaymaz.

Önerilen pano: Backlog → Hazır → Yapılıyor → İnceleme → Bitti. Engellenen iş, nedeni ve ihtiyaç duyduğu kararla ayrıca işaretlenir. Aynı anda bir ana geliştirme işi ve bir bağımsız içerik işi önerilir. Pano şu an dokümandaki iş listesidir; GitHub Issues/Projects henüz oluşturulmadı.

## Aşamalar ve bağımlılıklar

| Aşama | Çıktı | Geçiş ölçütü | Bağımlılık |
|---|---|---|---|
| 0 — Ürün kararları | Hedef kullanıcı, şehir, özellik kapsamı, bütçe | Ürün sahibi açık soruları yanıtlar | Yok |
| 1 — İçerik ve UX keşfi | Pilot veri, görüşme bulguları, iki tasarım yönü | Hangi bilgiyle karar verildiği ve içerik üretim maliyeti görünür | Aşama 0 |
| 2 — Prototip | Mobil/masaüstü tıklanabilir ana akış | Kullanılabilirlik testleri ve tasarım seçimi | Aşama 1 |
| 3 — Teknik temel | İçerik veritabanı, yönetici girişi, medya altyapısı ve kontrol akışı | İlk gerçek ve izinli kayıt uygulamada uçtan uca görüntülenir | Aşama 0–2 |
| 4 — Dikey MVP | Yönetim paneli, fotoğraf/etiket, keşif, filtre, detay ve sürümlü yayın | İş kuralları ve temel hata durumları doğrulanır | Aşama 3 |
| 5 — Kapalı beta | Kontrollü içerik grubu ve test raporu | Kritik sorunlar çözülmüş; yayın kararı verilmiş | Aşama 4 |
| 6 — Portföy ve tanıtım | Doğru iddialı vaka çalışması; onaylanırsa demo | Gizlilik/medya hakları/yayın kontrolleri geçer | Aşama 5 |

## Takvim nasıl kesinleşecek?

Şu an yayın tarihi taahhüdü yok. Haftalık ayrılacak süre, editör sayısı, içerik pilotu ve üyelik kararı bilinmiyor. İlk çalışma döngüsü için hedef: kapsam kararları + pilot örnek + ana akış taslağı. İkinci döngü: tasarım karşılaştırması + tıklanabilir prototip + gözlem. Döngü uzunluğu kapasiteye göre seçilecek.

İçerik tahmini, pilotta kaydedilen kayıt başına araştırma ve inceleme süresiyle hesaplanır: kalan kayıt sayısı × medyan süre + sorunlu kayıtların ek kontrolü. Yazılım tahmini seçilmiş akış ve entegrasyonlara göre ayrı yapılır. Tüm 235 kaydın aynı anda eksiksiz olması ile erken beta arasındaki tercih ürün sahibine sunulur.

## Başlangıç backlog'u

| ID | Öncelik | İş | Kabul ölçütü | Bağımlılık |
|---|---|---|---|---|
| GD-001 | P0 | MVP kararlarını kapat | Hedef kullanıcı/şehir/üyelik/dil ve sınırlar yazılı | Ürün sahibi |
| GD-002 | P0 | Repo hedefini kesinleştir | Hesap, ad, görünürlük ve veri sınırı belirli | Ürün sahibi |
| GD-003 | P0 | Pilot içeriği seç ve işle | Her kayıtta kanıt/durum; araştırma süresi raporu | GD-001 |
| GD-004 | P0 | Karar akışını tasarla | Liste, filtre, detay, geri dönüş ve boş durum incelenebilir | GD-001 |
| GD-005 | P0 | İki görsel yön hazırla | Aynı gerçek içerik üzerinde mobil ana/detay karşılaştırması | GD-003,004 |
| GD-006 | P0 | Prototipi test et | Görev bazlı gözlemler, başarısızlıklar ve kararlar kaydedilmiş | GD-005 |
| GD-007 | P0 | Mimari/sağlayıcı kararları | Bütçe, seçenek ve gerekçesi olan ADR'ler onaylı | GD-001,003,006 |
| GD-008 | P0 | Veri sözleşmesini doğrula | Geçerli veri kabul; bozuk kimlik/tarih/puan/koordinat reddedilir | GD-003 |
| GD-009 | P0 | Yayın çıktısını üret | Draft ve iç notlar dışarı çıkmaz; kimlikler korunur | GD-007,008,019 |
| GD-010 | P0 | Keşif ve filtreyi geliştir | Filtre birleşimi, temizleme, sonuçsuz durum, geri dönüş çalışır | GD-006,009 |
| GD-011 | P0 | Mekân detayını geliştir | Kaynaklı içerik, eksik medya ve bozuk bağlantı davranışı doğru | GD-006,009 |
| GD-012 | P0 | İçerik düzeltme/yayın süreci | Panelden düzeltme ve önceki sürümden taslak oluşturma denenir | GD-009,019 |
| GD-013 | P0 | Beta doğrulaması | Ziyaretçi ve yönetici akışları, yetki, medya, geri dönüş ve mobil kontroller kayıtlı | GD-010–012,015–019,021,022,028 |
| GD-014 | P1 | Portföy vaka çalışması | Gerçek katkı, kararlar, ekranlar ve ölçülmüş sonuçlar ayrılmış | GD-013 |


## Yönetim ve keşif için eklenen işler

P0 ilk çalışan MVP için gerekli; P1 beta sonrasında sıraya alınan öneri. Bu tablo geliştirme planıdır, özelliklerin tamamlandığı anlamına gelmez.

| ID | Öncelik | İş | Bittiğini nasıl anlayacağız? | Bağımlılık |
|---|---|---|---|---|
| GD-015 | P0 | Yönetici girişi ve sunucu yetkileri | Giriş yapan yönetici çalışır; oturumsuz düzenleme/yükleme/önizleme/yayın reddedilir | GD-007 |
| GD-016 | P0 | Mekân listesi ve düzenleme formu | Şehir/isim/durumla bul; yeni kayıt ekle; düzenle; taslak yeniden açılınca kalır; çakışma sessizce ezilmez | GD-008,015 |
| GD-017 | P0 | Fotoğraf ve video yönetimi | Fotoğraf yükle, kapak/sıra/açıklama seç; geçersiz dosya reddedilir; izinsiz medya yayımlanmaz | GD-015,016 |
| GD-018 | P0 | Etiket sözlüğü ve mekâna atama | Çoklu ekle/çıkar; tekrar engeli; ad değişince kimlikler korunur; kanıt ve tarih saklanır | GD-015,016 |
| GD-019 | P0 | Taslak, önizleme, yayın ve geçmiş | Taslak canlıyı değiştirmez; yayın tutarlı geçer; eski sürüm yeni taslak olur; özel önizleme korunur | GD-016,017,018 |
| GD-020 | P1 | Temalı seçkiler ve kısa yerel hikâyeler | Editör liste adı/açıklama/sıra belirler; yalnız yayımdaki kayıtlar görünür; rota iddiası yok | GD-019,013 |
| GD-021 | P0 | Yemek kaydı ve yemekten mekâna keşif | Araştırılmış yemeği seçince ilişkili yayımdaki mekânlar gelir; yalnız addan yemek üretilmez | GD-003,008,016 |
| GD-022 | P0 | Etiket filtreleri | Aynı grup VEYA, gruplar arası VE; sayı/temizleme/boş sonuç; taslak ve süresi geçmiş atama görünmez | GD-010,018,019 |
| GD-023 | P1 | Bilgi düzeltme bildirimi | Bildirim incelemeye düşer; doğrudan yayını değiştirmez; kötüye kullanım kontrolü var | GD-013,019 |
| GD-024 | P1 | Daha sonra gitmek üzere kaydetme denemesi | Kalıcılık ve hesap ihtiyacı kararlaştırılır; cihazda tutmanın sınırı açık gösterilir | GD-013; ürün kararı |
| GD-025 | P1 | Ziyaretçi popülerliği etiketinin kanıt yöntemi | Kaynak, dönem, örneklem ve değerlendirme ölçütü yazılı; kanıt yoksa rozet yayımlanmaz | GD-018; yeterli veri |
| GD-026 | P0 | Sosyal hesap ve video içeriğini doğrula | Doğru şube, kaynak ve video gömme uygunluğu kontrol edilir; doğrulanmamış hesap yayımlanmaz | GD-003,017 |
| GD-027 | P0 | Google Places sunucu entegrasyonu | İşletme eşleşmesi, sınırlı alan seçimi, erişim ve harcama sınırı; anahtar istemciye gitmez | GD-007; erişim/bütçe kararı |
| GD-028 | P0 | Canlı puan/yorum ve medya davranışı | Google verisi atıflı; eksik/hata durumları doğru; gerçek video oynatımı ve kapatınca durma denenmiş | GD-011,026,027 |

### Bundan sonraki teslim sırası

1. Panelde kayıt düzenleme → fotoğraf/etiket → önizleme akışını taslak ekranlarla netleştir.
2. Hazır içerik yönetimi ile özel paneli bu akış üzerinden karşılaştır; aylık bütçe ve teknoloji kararını kapat.
3. Yönetici girişi, kayıt formu, medya ve etiketleri çalıştır.
4. Yayın çıktısını keşif arayüzüne bağla; yemek ve etiketle aramayı tamamla.
5. Senin bir kaydı baştan sona yönetebildiğin ve ziyaretçinin onu bulabildiği küçük betayı dene.

Panel ve medya yönetimi yeni geliştirme işi ekliyor. Önceki planda kesin süre verilmemişti; aynı kapsamı aynı sürede bitireceğimizi varsaymıyoruz. İlk tahmini GD-015–019 akışının teknoloji seçimiyle birlikte çıkaracağız.

## İşe başlama ve bitirme kuralları

Bir iş hazır sayılmak için kullanıcı ihtiyacı, kapsam, gözlenebilir kabul ölçütü ve bağımlılıkları belli olmalıdır. Bitti sayılmak için ilgili akış çalıştırılmış, önemli hata durumları görülmüş, veri/erişim sınırı korunmuş ve bulgular yazılmış olmalıdır. Kod yazılması tek başına tamamlanma değildir.

Haftalık önerilen kısa değerlendirme: ne çıktı, hangi varsayım değişti, ne engelliyor, sıradaki küçük teslim ne? Kapsam değişikliği iş listesi ve tahmini günceller; gizlice MVP'ye eklenmez.
