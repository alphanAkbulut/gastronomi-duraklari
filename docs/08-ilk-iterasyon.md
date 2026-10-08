# İlk prototipte ne denedik? — 8 Ekim 2026

## Nereden başladık?

- İlk akışı İstanbul’da yaşayan ve o gün nerede yemek yiyeceğine karar vermeye çalışan biri için hazırladık. Üyelik eklemedik; önce keşif deneyimini görmek istedik. Bu tercihler prototipin başlangıç noktası, nihai kapsam kararı değil.
- Kaynak listeden 20 kayıt ayırdık. 16’sını iki tasarımda da kullandık; dört kayıttaki çelişki ve eşleşme sorularını önce incelemek üzere ayrı tuttuk.
- Sofra Defteri: açık zemin, serif başlıklar ve iki sütunlu editoryal liste. Mahalle Panosu: koyu yeşil giriş, sans serif ve kompakt kartlar. Aynı veri ve etkileşimler kullanılıyor.
- Arama, ham adres içinde bölge filtreleme, detay, iki adayı karşılaştırma, üçüncü seçimi engelleme ve sonuçsuz arama durumları eklendi.
- GitHub'da private repo oluşturuldu; kod yükleme onayı ayrı bekleniyor.

## Veriyle çalışırken karşımıza çıkanlar

İstanbul listesinde adresi Konya görünen bir kayıt bulduk. Ayrıca farklı mekânların aynı harita bağlantısını paylaştığı ve benzer isimlerin eşleştirmeyi zorlaştırdığı örnekler var. Bunları otomatik düzeltmek veya birleştirmek yerine inceleme listesine aldık. Orijinal kaynak kayıtlarını koruduk.

Bölge filtresi şimdilik ham adresin içinde arama yapıyor. Henüz doğrulanmış bir ilçe alanımız olmadığı için düğmeyi de buna göre adlandırdık. Yemek önerisi, puan ve medya araştırması sonraki işimiz; bu prototip o bilgilerin yerini tutmuyor.

## Tarayıcıda neyi kontrol ettik?

| Kontrol | Gözlenen sonuç |
|---|---|
| `ciya` araması | Türkçe Ç/ı dönüşümüyle tek ilgili kayıt |
| Detay aç/kapat | Kaynak bilgisi ve eksik içerik durumları görünür; arama korunur |
| Kadıköy filtresi | Pilot içinden üç eşleşme |
| İki aday seçme | İki aday karşılaştırma penceresinde görünür |
| Üçüncü aday | Engellenir; kullanıcıya açıklama gösterilir |
| Sonuçsuz arama ve temizleme | Boş durum görünür; temizleyince 16 kayıt |
| Escape ile kapatma | Pencere kapanır; odak açan düğmeye döner |
| 390 × 844 mobil | Her iki yönde sayfa genişliği = içerik genişliği, yatay taşma yok |
| Mobil detay | 350 px görünür/iç genişlik; taşma yok, odak kapatma düğmesinde |
| Tarayıcı hata günlüğü | Kontrol sırasında hata kaydı yok |

Bu denemeler temel akışların çalıştığını gösteriyor. Henüz hedef kullanıcılarla görüşmedik ve kapsamlı bir erişilebilirlik testi yapmadık. Tasarımın gerçekten daha iyi yemek kararları verdirdiğini söylemek için kullanıcı gözlemine ihtiyacımız var.

## Sırada ne var?

1. Ürün sahibinin iki görsel yöne tepkisi; gerekirse beğendiği referanslarla yeniden tasarım.
2. Pilot mekânların şube/adres, yemek önerisi, resmî hesap ve medya araştırması. Puan/medya şartları seçilen sağlayıcıya göre kontrol edilecek.
3. Kaynaklı içerik geldiğinde detay ve karşılaştırmanın karar verdirme gücünü yeniden test etme.
4. Haftalık kapasite, servis bütçesi ve üretim mimarisi kararı; ücretli servis açılmadı.
5. Kodun private GitHub reposuna ilk commit/push için açık onay. Gerçek restoran verisi, yerel çıktı ve ekran görüntüleri yüklemeye dahil değildir.
