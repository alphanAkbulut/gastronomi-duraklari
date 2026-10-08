# Mekân detayında konuştuğumuz bilgiler nerede duracak?

İlk prototip bu kısmı fazla kısa geçmişti. Sosyal hesap, video ve puanları tek bir “araştırma bekliyor” metninde toplamak, ürünün asıl değerini göstermiyordu. İkinci sürümde bu alanlar ayrı bölümler olarak yer alıyor.

## Sayfa düzeni

| Bölüm | Ziyaretçi ne görecek? | Bu sürümde ne çalışıyor? |
|---|---|---|
| Genel bakış | Ne yenir, neden gidilir | Alanlar ve açık boş durum; editör içeriği henüz yok |
| Fotoğraflar | Yemek, mekân ve ayrıntı galerisi | Üç yer tutucu; gerçek fotoğraf yükleme/render entegrasyonu bu turda yapılmadı |
| Instagram | Mekânın doğrulanmış hesabına giden bağlantı | Doğrulanmış hesap verisini taşıma ve güvenli bağlantı yolu eklendi; pilot kayıtların hesabı boş |
| YouTube | 2–3 ilgili video; sayfa içinde oynatıcı ve YouTube’a git bağlantısı | Uygun video verisi gelirse oynat düğmesi iframe oluşturur; pilotta henüz video yok, gerçek oynatma testi yapılmadı |
| Google puanı ve yorumlar | Puan, toplam değerlendirme sayısı, yorumlar ve kaynak bağlantısı | Yerleşim ve boş durum hazır; API çağrısı ve veriyle dolu yorum bileşeni henüz yok |
| Ziyaret bilgileri | Adres, saat, telefon, resmî site ve son kontrol | Kaynak adresi var; diğer alanların boş durumu gösteriliyor |

Üstteki bölüm düğmeleri sayfanın ilgili kısmına götürüyor. İçerik olmayan Instagram/Google düğmeleri pasif; varmış gibi başka bir şubeye veya arama sonucuna yönlendirmiyoruz. Detay kapanınca içeriği kaldırıyoruz; böylece ileride açılmış bir video arka planda kalmıyor.

## Instagram ve YouTube

Instagram’da ilk hedef hesabı dış bağlantıyla açmak. Gönderi gömme veya Instagram’dan fotoğraf indirme bu işin parçası değil. Hesap doğrulaması yanlış şubeye gitmeyi önlemek için gerekli.

YouTube bağlantısı desteklenen alan adından ve geçerli video kimliğinden oluşturulur; panelden gelen keyfî HTML çalıştırılmaz. Oynatıcı, kullanıcı düğmeye bastığında yüklenir. Video burada oynatılamazsa dış bağlantı durur. Gömülü oynatıcı yolu YouTube’un kendi dokümantasyonuna dayanır. [YouTube iframe parametreleri](https://developers.google.com/youtube/player_parameters?authuser=2&hl=en).

Mevcut v1 veri sözleşmesinde ayrı bir `embed_allowed` alanı yok. Prototip, doğrulanmış ve hak durumu olumlu video kayıtlarını kabul ediyor. Bu kontrol tek başına YouTube gömme iznini kanıtlamaz; canlı entegrasyonda videonun hâlâ erişilebilir ve gömmeye açık olması ayrıca kontrol edilmeli. İzin verilmiş videonun gerçek oynatımını doğrulamadan entegrasyonu tamamlandı saymayacağız.

## Google’dan ne alacağız?

Place Details ile işletme adresi, telefon, puan ve yorum gibi alanlar alınabiliyor. İstek alanlarını ihtiyaca göre seçmek gerekiyor; her alanın bulunacağı varsayılmaz. Bizim kaynak adresimiz ile Google’dan gelen adres ayrı tutulacak; doğru şube eşleştirilmeden puan gösterilmeyecek. [Place Details](https://developers.google.com/maps/documentation/places/web-service/place-details?authuser=3), [veri alanları](https://developers.google.com/maps/documentation/places/web-service/data-fields?hl=en).

Yorum kartında yazar, tarih, puan, metin ve kaynak/atıf alanı birlikte ele alınacak. API sonucu Google’daki bütün yorumların bir kopyası sayılmayacak. Google verisi kendi editör değerlendirmemize dönüştürülmeyecek; gösterim ve saklama kuralları entegrasyonun kabul koşulu olacak. [Google Places gösterim ve atıf kuralları](https://developers.google.com/maps/documentation/places/web-service/policies?hl=en).

Bu sürüm Google’a istek atmıyor. API anahtarı alınmadı, faturalandırma açılmadı. Çalışma saatleri, puanlar ve yorumlar için sunucu entegrasyonu ayrı iş olarak duruyor.

## Sonraki uygulama işleri

- GD-026: Pilot şubelerin resmî sosyal hesaplarını ve ilgili videolarını doğrula; kaynağıyla panele ekle.
- GD-027: Google işletme eşleştirmesi, istenen alanlar ve harcama sınırı için sunucu entegrasyonunu kur. Sağlayıcı seçimi/erişim/bütçe kararı gerekir.
- GD-028: Google’dan gelen dolu, eksik ve hatalı sonuçları ekranda göster; yorum atıflarını ve gerçek YouTube oynatımını doğrula.

Ekranın yerleşimiyle canlı veri entegrasyonunu ayrı takip ediyoruz. İlkini hazırladık; ikincisinin tamamlandığını söylemiyoruz.
