# Ürün kapsamı — başlangıç taslağı

## Problem ve amaç

Yemek seçerken bilgi pek çok yere dağılır: restoran sayfası, sosyal medya, harita yorumları ve videolar. Kullanıcının bir günde deneyebileceği yemek sayısı sınırlıdır; yanlış seçim maliyeti yalnızca para değildir. Ürün, lezzet seçeneklerini anlamlı gerekçeler ve kanıtlarla bir araya getirerek seçim yapmayı kolaylaştırmayı amaçlar. Memnuniyet garantisi veya nesnel bir “en iyi restoran” iddiası taşımaz.

## Kullanıcı tarafından belirtilmiş yön

- Yerel, samimi ve farklı bütçelere açık keşif; lüks zorunlu değil.
- UI ve UX ürünün başlıca fark yaratma alanı.
- Bakanlık seçkisi başlangıç kaynağı; tüm şehirler saklanacak.
- Mekân sayfasında adres, ne yenir, neden tercih edilir, kaynaklı puan ve varsa sosyal hesap/gerçek fotoğraf/ilgili video bir araya gelsin.
- Michelin kesişimi daha sonra incelenebilir; temel ürün odağı değil.
- Sesli tur ve gelişmiş rota MVP önceliği değil.
- Yönetici panelinden mekânları düzenleme, fotoğraf ekleme ve etiket atama ilk sürümün parçası. Ziyaretçi üyeliğiyle yönetici girişini ayrı ele alıyoruz.

## Karar bekleyen MVP önerisi

İstanbul’da günlük yemek kararı veren kullanıcılar; Türkçe, mobil öncelikli web deneyimi. Üyeliksiz keşif, arama/filtre ve mekân detayı. Şehir kapsamı ve üyelik kararı henüz onaylanmadı. Veri modelinin çok şehirli olması tüm şehirleri aynı anda yayımlama zorunluluğu yaratmaz.

### Temel kullanıcı işleri

| İhtiyaç | Ürün davranışı | Gözlenebilir kabul ölçütü |
|---|---|---|
| Aklımdaki yemek veya bölgeye göre seçenek bulmak | İsme göre arama; yalnızca doğrulanmış alanlardan yemek/bölge filtreleri | Birden çok filtre birlikte işler, temizlenebilir; eşleşme yoksa neden ve çıkış yolu gösterilir |
| Buraya neden gitmeliyim? | Kısa gerekçe, önerilen yemek, adres, kaynak ve güncellik | Kaynakta olmayan bilgi üretilmez; eksik alan puan sıfır veya olumsuz değerlendirme olarak görünmez |
| Seçenekler arasında karar vermek | Aynı bilgi sırasına sahip kartlar; ayrı karşılaştırma ekranı UX testiyle kararlaştırılır | Kullanıcı iki adayı aynı ölçütlerle açıklayabilir; listeye dönüşte filtre ve konum korunur |
| Nasıl ulaşırım? | Doğrulanmış harita bağlantısı | Eksik/şüpheli bağlantı aktif yol tarifi butonu olarak yayımlanmaz |
| Bilgiye güvenmek | Sağlayıcı adı, gözlem zamanı ve editoryal/sağlayıcı ayrımı | Bir sağlayıcı puanı başka sağlayıcıdan gelmiş gibi gösterilmez; ziyaret edilmemiş mekân ziyaret edilmiş gibi yazılmaz |

İlk sürümde bütçe, yakınlık, açık olma ve diyet filtreleri ancak veri yeterli ve doğrulanmışsa açılır. Şu an veri setinde bunların dolu olduğu varsayılmaz. Özellikle alerjen güvenliği çıkarımı yapılmaz.

## Sonraki aşamalara bırakılması önerilenler

Üyelik/favoriler karara bağlıdır. Kullanıcı yorumları, otomatik kişiselleştirme, rezervasyon/ödeme, animasyonlu rota, turist rehberi, Michelin sekmesi, restoran işletmecilerinin kullanacağı panel ve ücretli ürünler başlangıç kapsamına alınmaz. Gelir modeline ilişkin hipotezler gerçek kullanım görüldükten sonra ayrı değerlendirilir.

## Başarıyı nasıl ölçeceğiz?

Önerilen ilk kullanıcı testinde 5 hedef kullanıcıdan en az 4'ünün, yönlendirme almadan 3 dakika içinde iki seçenek bulup birini gerekçesiyle seçmesi. Bu bir başlangıç hedefidir, elde edilmiş sonuç değildir. İkinci kontrol: katılımcı kaynak puanını editoryal görüşten ve eksik bilgiden ayırabiliyor mu?

Beta sonrasında: anlamlı filtre kullanımı, detay inceleme, haritada açma ve kısa karar güveni sorusu. Haritada açma gerçek ziyaret veya memnuniyet kanıtı değildir. Hedefler ilk gözlemlere göre güncellenir; yapay trafik ve ekip denemeleri ayrı tutulur.

## İçerik yönetimi de ürünün bir parçası

İlk sürümde kayıtları sen yönetebileceksin: ekle/düzenle, etiket seç, fotoğraf yükle, taslağı kaydet, önizle ve yayımla. Yayındaki bir kaydı düzenlemek mevcut sayfayı anında değiştirmeyecek. Bu ihtiyaç, ziyaretçilerin hesap açmasını gerektirmiyor.

Ayrıntılar [yönetim paneli](10-yonetim-paneli.md) ve [etiket kuralları](11-etiketler.md) belgelerinde. Benzer ürünlerden aldığımız fikirler [araştırma notunda](09-benzer-urunler.md); çekirdek MVP ile sonraki denemeler ayrı sıralandı.
