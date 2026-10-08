# Benzer ürünlerden ne alabiliriz?

8 Ekim 2026’da dört ürünün herkese açık sayfalarını ve kendi yardım belgelerini inceledim. Amacım özellik sayısını artırmak değil; yemek seçerken gerçekten işe yarayan birkaç fikri bulmak. Aşağıdaki “gözlem” satırları kaynakta görülenleri, “bizde” kısmı ise önerimizi anlatıyor. Kapalı yönetim panellerine giriş yapmadım; bu paneller hakkındaki bilgiler ürünlerin kendi açıklamalarından geliyor.

## Dört farklı yaklaşım

| Ürün | Kaynakta gördüğüm | Bizde ne işe yarar? |
|---|---|---|
| The Infatuation | Mekânların yanında “Perfect For” başlığıyla öğle yemeği, buluşma, tek başına yemek gibi kullanım durumları; bölge, mutfak, fiyat göstergesi ve kısa editoryal metin var. | “Hangi durumda burayı seçerim?” sorusuna cevap veren etiketler ve kısa gerekçeler. |
| TasteAtlas | Yemek listesinden, o yemekle ilişkilendirilen mekânlara geçilebiliyor. | Kullanıcı mekân adını bilmese de “iyi bir pide yemek istiyorum” diye başlayabilir. |
| HappyCow | Kendi uygulama yardımında beslenme türü ve mesafe filtrelerini anlatıyor. İşletme yardımında bilgi düzenleme, fotoğraf ekleme ve değişiklik önerme yolları var. | Kontrollü filtreler, düzenlenebilir içerik ve zamanla “bilgi yanlış” bildirimi. İşletme sahiplerine hesap açmak ilk sürüm için gerekli değil. |
| Gastro Obscura / Atlas Obscura | Yerel yemek hikâyeleri ve sıra dışı mekânlar öne çıkıyor. Atlas Obscura katkı yönergesinde düzenleme önerisi, taslak ve yayın öncesi editoryal inceleme anlatılıyor. | “Bu yeri özel yapan ne?” metni ve yayın öncesi kontrol. Gastro veritabanının bugün ağırlıkla kendi ekibince yazıldığını ayrıca belirtiyorlar; iki katkı modelini aynı saymıyoruz. |

Kaynaklar: [The Infatuation — örnek bölge rehberi](https://www.theinfatuation.com/new-york/guides/best-hells-kitchen-restaurants), [TasteAtlas — yemek ve mekân bağlantısı](https://www.tasteatlas.com/best/dishes), [HappyCow — uygulama yardımı](https://www.happycow.net/mobile/android), [HappyCow — işletme yönetimi](https://www.happycow.net/business/faq), [Atlas Obscura — katkılar ve Gastro Obscura](https://www.atlasobscura.com/faq).

Bunlar kapsamlı bir pazar araştırması veya ücretli üyelik karşılaştırması değil. Herkese açık örneklerde gözlenmeyen işlevleri bu ürünlere atfetmedim. Sayfalardaki sıralama, puan ve içerikleri kendi katalogumuza aktarmıyoruz.

## Bizim plana aldıklarım

| Özellik | Neden alıyoruz? | Sıra / iş |
|---|---|---|
| Mekân yönetimi, fotoğraf yükleme, önizleme ve yayın | Her düzeltme için geliştiriciye ihtiyaç kalmasın. Kullanıcının doğrudan talebi. | MVP, GD-015–019 |
| Kontrollü etiketler ve etiketle filtreleme | Aynı ihtiyacın farklı yazımlarla dağılmasını önler; seçim yapmayı hızlandırır. Kullanıcının doğrudan talebi. | MVP, GD-018 ve GD-022 |
| Ne yenir + neden gidilir + gitmeden bil | Karar için puanın yanında somut bilgi gerekir. Önceki ürün hedefinin parçası. | MVP, GD-011 ve GD-021 |
| Yemekten mekâna keşif | Mekân ismi bilmeyen kullanıcı da başlayabilir. | MVP içinde küçük kapsam, GD-021; yalnız araştırılmış yemekler |
| Editörün hazırladığı temalı listeler | “Kadıköy’de tatlı molası” gibi bir başlangıç sunar; bunlar rota değildir. | İlk beta sonrası öneri, GD-020 |
| Kısa yerel hikâye | Yerle bağ kurdurur; kaynak varsa, detayı gereksiz uzatmadan. | Beta içerik denemesi, GD-020 |
| Bilgi düzeltme bildirimi | Adres ve kapanma gibi hataları kullanıcıdan öğrenebiliriz. | Beta sonrası, GD-023; inceleme kuyruğuyla |
| Sonra gitmek üzere kaydetme | Beğenilen aday kaybolmasın. | Beta sonrası seçenek, GD-024; üyelik kararı ayrıca |
| Ziyaretçi popülerliği etiketi | Kullanıcının sorduğu örneği veriyle destekleyebilirsek anlamlı olur. | GD-025; kanıt yöntemi belirlenene kadar yayına kapalı |

## Şimdilik almadıklarım

Açık kullanıcı yorumları ve yıldız sistemi moderasyon işi getiriyor. Rezervasyon/ödeme, restoran sahiplerinin kendi paneli, ücretli öne çıkarma ve otomatik rota farklı problemler çözüyor. Şimdiki öncelik, senin güvenilir bir seçkiyi kolayca yönetebilmen ve ziyaretçinin karar verebilmesi.

Başka sitelerdeki sayısal puanları tek bir “bizim puanımız” içinde eritmek de önerim değil. Kaynağı ve zamanı belli puan ile bizim editoryal değerlendirmemiz ayrı kalmalı.

## Bu sırayı nasıl kontrol edeceğiz?

Panelde bir mekânın adresini düzeltip fotoğraf ve etiket ekle; taslağı kaydet, önizle ve yayımla. Ziyaretçi tarafında aynı mekânı yemek/etiket filtresiyle bul ve neden seçebileceğini anla. Bu iki akış sorunsuz tamamlanmadan yeni özellik eklemeye öncelik vermeyelim.
