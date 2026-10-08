# Gastronomi Durakları — başka bir yapay zekâ için proje aktarımı ve analiz promptu

Bu dosyayı diğer yapay zekâ aracına yükleyebilir veya içeriğini tek mesaj olarak yapıştırabilirsin. Aşağıdaki metin doğrudan o araca hitap eder. Proje durumu 8 Ekim 2026 tarihli konuşma, yerel belgeler ve veri raporlarına dayanır. Bu dosya restoran veri setinin kendisini içermez.

---

## 1. Senden istediğim

Benimle bu projeyi deneyimli bir ürün yöneticisi, UX/UI tasarımcısı ve yazılım geliştiricisi gibi değerlendir. Önce aşağıdaki bağlamı bütünüyle oku. Mevcut planı doğru kabul edip tekrar anlatmanı istemiyorum. Eksiklerini, yanlış önceliklerini ve gereksiz karmaşıklığını eleştir; uygulanabilir bir yol öner.

Asıl sorum şu: **Bu ürünü, başka bir restoran listesinden farklı olarak insanların gerçekten kullanacağı bir yemek karar yardımcısına nasıl dönüştürürüz?**

Özellikle şu konulara cevap istiyorum:

- Ürünün somut değeri ve kaynak siteden farkı.
- Gerçek içerikle çalışan, sıcak ve özgün bir kullanıcı deneyimi.
- Mekân bilgisi, fotoğraf, sosyal hesap, video ve değerlendirmelerin güvenilir biçimde toplanması ve güncel tutulması.
- Benim yönetebileceğim bir admin/backoffice.
- Küçük başlayabilecek, geliştirilebilir bir teknik mimari ve veri modeli.
- Gerçekçi MVP, iş sırası, maliyet/efor varsayımları ve tamamlanma ölçütleri.
- Kullanıcının güvenini bozmadan para kazanma seçenekleri.
- Sürecin ve ürünün portföyüme dürüstçe eklenmesi.

Türkçe, açık ve doğal yaz. Genel girişimcilik tavsiyeleri, şişirilmiş kurumsal metinler, boş övgüler ve uzun özellik listeleri istemiyorum. Somut öneri ver; nedenini ve ödünleşimini açıkla. Anlatılmış bilgileri yeniden sorma. Yalnız kararı gerçekten değiştirecek eksik bilgiler için en fazla beş öncelikli soru sor; diğer konularda varsayımını belirterek ilerle.

Bu istek analiz ve incelenebilir öneri hazırlama isteğidir. Hesap açma, ücretli servis başlatma, mevcut dosyaları değiştirme, commit/push veya yayınlama yetkisi vermez. Güncel servis, fiyat, rakip ve kullanım koşulu iddialarını araştırabiliyorsan birincil kaynaklarla doğrula. İnternet erişimin yoksa bunu belirt ve güncelmiş gibi bilgi uydurma. Ekte olmayan dosyaları ya da localhost sayfasını gördüğünü iddia etme.

## 2. Ürünün çıkış noktası

Çalışma adı **Gastronomi Durakları**. Temel problemimiz günlük hayattaki “Nereye gitsek, ne yesek, orası güzel midir?” kararsızlığı.

Bir insanın bir günde yiyebileceği öğün sayısı sınırlı. Kötü bir seçim yalnızca para kaybı değil; zamanı, iştahı ve günün deneyimini de tüketiyor. İki kötü seçim bütün günü bozabiliyor. Kullanıcıyı haritalar, sosyal medya ve videolar arasında dolaşmaktan kurtarıp kararını güçlendirmek istiyoruz.

Ürünün bana ait ana tarifi: **“Biz karar mekanizmasını güçlendiriyoruz ve güzellikleri bir arada gösteriyoruz.”**

Mekân isimlerini sıralamak yeterli değil. Kullanıcı şunları anlamalı:

1. Burada ne yemeliyim?
2. Neden burayı seçebilirim; burayı özel yapan ne?
3. Hangi beklentiyle gitmeliyim; gitmeden ne bilmeliyim?
4. Hangi durumda ve kimin için uygun olabilir?
5. Bunu destekleyen gerçek görüntü, video ve değerlendirme var mı?
6. Diğer adayla arasındaki anlamlı fark ne?
7. Adres ve ulaşım bilgisine güvenebilir miyim?

“Gidilir/gidilmez” kararını desteklemek istiyorum; fakat kanıtsız hüküm veya herkese aynı zevki dayatan yapay bir puan istemiyorum. Araştırmaya dayanan yorum, kişisel ziyaret deneyimi ve dış platform puanı birbirine karışmamalı.

## 3. Üslup, hedef kitle ve konumlandırma

Yerel, samimi, sıcak bir yemek keşfi istiyorum. Pahalı veya lüks restoran olması gerekmiyor. Fırın, esnaf lokantası, dönerci, tatlıcı ve kahveci de deneyimin parçası olabilir.

Michelin benim için temel kalite ölçütü değil. Kültür Yolu listesini daha yerel bir başlangıç olarak beğendim. Bu, listenin hatasız veya tüm iyi mekânları kapsadığı anlamına gelmiyor.

İstanbul’da günlük yemek kararı veren kişiler mevcut prototipin başlangıç varsayımı. Türkçe ve mobil öncelikli, ziyaretçi üyeliği gerektirmeyen bir ilk sürüm önerildi. Bunlar nihai olarak onaylanmış bütün ürün kararları değil. Turistler, İngilizce deneyim, başka şehirlerin yayına alınması ve ziyaretçi hesabı ayrı kararlar.

Veri tüm mevcut şehirlerden arşivlendi. Bunun anlamı ilk gün bütün şehirleri yayımlamak zorunda olduğumuz değil. İstanbul’dan başlarken çok şehirli yapıyı korumak istiyoruz.

## 4. UI/UX beklentim ve mevcut çalışmadan duyduğum memnuniyetsizlik

Bu projede en fazla önem verdiğim alan UI ve UX. Figma kullanmayı bilmiyorum; tasarım araçlarını öğrenmek projenin ilerlemesinin ön şartı olmamalı. Tıklanabilir örnekler ve gerçek içerik üzerinden karar verebilmeliyim.

Önceki yapay zekâ çıktıları bana fazla genel, şablon ve “AI slop” göründü. Yalnız renk, font, yuvarlatılmış kart ve rozet değiştirmek ürün tasarımı sayılmamalı. Güzel görünen ama ne seçeceğimi anlatmayan bir sayfa istemiyorum.

Mevcut prototipte 16 mekân vardı; çoğunda yalnız ad/adres ve boş içerik bölümleri bulunuyordu. Bu yüzden şu itirazları yaptım:

- Neden bu kadar az mekân var?
- Dönerci Sadık Usta neden yok?
- Konuştuğumuz Instagram yönlendirmeleri, gömülü YouTube videoları ve Google yorumları nerede?
- Kaynak sitenin listesini daha eksik biçimde göstereceksek bizim katkımız ne?

Önceki asistan, dokümanlara ve yüzeysel prototipe fazla odaklandığını; mevcut deneyimin fikrin hakkını vermediğini kabul etti. Daha sonra **3–5 mekânı gerçekten araştırıp doldurarak tek bir güçlü keşif ve karar akışı hazırlamayı önerdi**. Bu içerik araştırması ve yeni deneyim henüz yapılmadı. Bu öneriyi uygulanmış veya benim kesin onayladığım yeni kapsam gibi kabul etme.

Analizinde bu başarısızlığı merkezde tut. Yeni boş kutular ve daha uzun bir backlog aynı problemi çözmez. Aynı zamanda 3–5 içerik örneği ile 235 kaydın tam katalog kapsamını ayrı ele al; örnek çalışmayı tam ürünmüş gibi sunma.

## 5. Kaynak liste ve veri arşivi

Başlangıç kaynağı:

https://kulturyolufestivali.com/taste-points/istanbul

İlk talebim, API bulunduğunu varsaymadan tarayıcıdaki kartları ve varsa pagination/load-more adımlarını dolaşmaktı. Sonra site kapanırsa bilgi kaybolmasın diye bütün mevcut şehirlerin toplanmasını istedim.

Mevcut çalışma kayıtlarına göre 8 Ekim 2026’da:

| Konu | Durum |
|---|---|
| Arşivlenen lezzet dizinleri | 21 şehir |
| Toplam kayıt | 1.118 |
| İstanbul | 235 |
| Taranan liste sayfası | 103 — önceki tarama raporundaki sayı |
| Harita bağlantısı eksik | 29 kayıt |
| Bağımsız mekân detay URL’si | 1.118 kayıtta yok; kaynak kartlarında bulunmadı |
| Gerçek fotoğraf/video/puan zenginleştirmesi | Henüz tamamlanmadı |

Şehir sayıları: Ankara 58, Aydın 43, Bursa 50, Erzurum 39, Eskişehir 33, Gaziantep 69, Kahramanmaraş 51, Kayseri 34, Konya 53, Malatya 31, Manisa 34, Mersin 46, Nevşehir 43, Ordu 42, Sakarya 50, Samsun 43, Trabzon 51, Van 27, Çanakkale 52, İstanbul 235, Şanlıurfa 34.

Festival tanıtımında 26 şehir bulunmasına rağmen lezzet dizininde 21 şehir vardı. **Adana, Antalya, Diyarbakır, İzmir ve Mardin** için lezzet dizini bulunmadı. Bu şehirleri taranmış, boş veya restoranı olmayan şehirler sayma.

Bu rakamlar arşiv kapsamıdır. Türkiye’deki tüm restoranları, tüm yerel iyi mekânları veya bugün hâlâ açık işletmeleri temsil etmez. Mevcut listenin eksiksizliği ile kaynağın kendisinin kapsamı farklı şeylerdir.

### Bilinen veri sorunları

- İstanbul listesindeki Prasini Papia kaydında Meram/Konya adresi vardı; prototip dışında incelemeye ayrıldı.
- Ginkgo Asian Dining ve Gözde Şarküteri farklı ad/adrese rağmen aynı harita bağlantısını taşıyordu.
- Karadeniz Döner ile Karadeniz Döner Asım Usta için olası eşleşme/şube sorusu var; otomatik birleştirilmedi.
- Loft Vakkoroma ve Morini aynı adresi taşıyor; farklı işletmeler olabilecekleri için yalnız adrese bakılarak birleştirilmedi.
- Ankara Beykoz İşkembecisi kaydında birleştirilmiş/bozuk harita URL’si görüldü; ham değer korundu ve işaretlendi.
- Önceki arşiv kontrolünde Dönerci Sadık Usta bulunmadı. Bu, işletmenin var olmadığı anlamına gelmez. Kaynaktaki Dönerci Şahin Usta ile aynı yer olduğu varsayılmamalı; doğru şube bilgisi hâlâ açık.

## 6. Dosyalar, repo ve gizlilik

Dosyaları kendi bilgisayarımda `Documents/gastronomiDuraklari/` altında tutmak istedim. Google Drive’a yüklenmiş doğrulanmış bir kopya yok. Başka insanların özel arşive erişmesini istemiyorum.

Mevcut yerel yapı:

```text
gastronomiDuraklari/
  istanbul_lezzet_noktalari.json
  lezzet_arsivi_2026-10-08/
    tum_sehirler.json
    sehirler/
    ham_kaynak/kaynak_kartlar.json
    kontrol_raporu.json
    ARSIVI_AC.html
    OKU_BENI.md
    SHA256SUMS.txt
  lezzet_arsivi_2026-10-08.zip
  lezzet_dataset_v1/
    dataset.json
    cities/
    identity_map.json
    venue.schema.json
    validation_report.json
    OKU_BENI.md
  lezzet_dataset_v1.zip
  proje/
    README.md
    AGENTS.md
    data-source-manifest.json
    schemas/venue.schema.json
    docs/
    prototypes/
    scripts/
    private/
```

Not: Alt dizin adlarının tamamını uygulamadan önce gerçek dosyalarla kontrol et; bu ağaç yön bulma içindir. Dosyalara bu prompt üzerinden erişimin yok. İhtiyaç olursa yalnız gerekli dosyaları istemelisin.

GitHub adresi: https://github.com/alphanAkbulut/gastronomi-duraklari

Önceki oturumda private repo oluşturuldu ve yerel Git bağlantısı kuruldu. Yerelde 8 Ekim kontrolünde henüz commit yoktu; proje dosyaları izlenmeyen dosyalar durumundaydı. İlk commit/push için açık onay alınmadı. Uzak repo bu aktarım hazırlanırken yeniden sorgulanmadı; uzaktaki güncel durumu kontrol etmeden değişmez kabul etme.

Gerçek katalog, ham kaynaklar, indirilen medya ve erişim anahtarları repoya eklenmiyor. Yerel arşiv, kod deposu, canlı demo ve bağımsız yedek farklı şeyler. Aynı bilgisayarda ZIP bulunması cihaz kaybına karşı yedek değildir. Yerel erişim kısıtları şifreleme anlamına gelmez; bağımsız özel yedekleme ve geri yükleme testi açık iş.

## 7. Bugün gerçekten ne var, ne yok?

| Alan | Mevcut durum |
|---|---|
| Ham arşiv ve ortak JSON veri seti | Var; 21 şehir / 1.118 kayıt |
| Yazılım dostu kayıt kimlikleri ve kaynak izi | Var |
| JSON Schema | Var; tam haricî şema doğrulaması yapılmadı |
| Ürün/UX/mimari/admin planları | Markdown belgeleri var; uygulamanın kendisi değiller |
| Tıklanabilir prototip | Var; 16 İstanbul mekânı |
| Pilot seçimi | 20 kayıt; 16 görünür, dört sorunlu kayıt incelemede |
| Arama, bölge seçimi, detay ve iki aday karşılaştırma | Prototip düzeyinde var |
| Instagram | Doğrulanmış bağlantıyı gösterecek yol var; gerçek pilot hesapları doldurulmadı |
| YouTube | Uygun veri gelince iframe oluşturacak kod var; gerçek pilot video ve canlı oynatma testi yok |
| Fotoğraflar | Yer tutucular var; gerçek galeri içeriği yok |
| Google puanı ve yorumları | Boş yerleşim var; API ve dolu yorum bileşeni yok |
| Araştırılmış “ne yenir / neden gidilir” içeriği | Pilot genelinde hazır değil |
| Backend ve veritabanı | Yok |
| Yönetici girişi / admin / fotoğraf deposu | Yok; gereksinimleri yazıldı |
| Canlı yayın / kullanıcı betası | Yok |
| Kullanıcı görüşmeleri ve ölçülmüş ürün başarısı | Yok |
| Monetizasyon | Seçilmedi, test edilmedi |

Prototipin iki görsel denemesi “Sofra Defteri” ve “Mahalle Panosu”. İlkinde krem/bordo ve serif, ikincisinde yeşil ve daha pano benzeri düzen denendi. Hiçbiri seçilmiş nihai tasarım sayılmamalı.

İkinci prototipte detay bölümleri eklendi: genel bakış, fotoğraflar, Instagram, YouTube, Google yorumları, ziyaret bilgileri. Bu, **gerçek içerik veya çalışan sağlayıcı entegrasyonu bulunduğu anlamına gelmiyor**.

Önceki yerel önizleme adresleri `http://127.0.0.1:8765/` ve ikinci sürüm için `/v2/` idi. Başka bilgisayardaki yapay zekâ bu adreslerden benim dosyalarıma ulaşamaz. Güncel sunucunun çalıştığı ayrıca kontrol edilmeli.

Mevcut kontroller: kimliklerin benzersizliği, şehir/toplam uyumu, kaynak alanlarının korunması, JSON okuma/yazma; prototipte arama, detay kapatma/odak, bazı klavye ve dar ekran akışları. Bunları gerçek kullanıcı testi veya tamamlanmış ürün testi sayma. İkinci sürümde istenen 390 px mobil genişlik araçta etkin 443 px olarak raporlandı; tam 390 px kontrolü doğrulanmış değil. Gerçek YouTube oynatma, Google entegrasyonu ve dolu medya akışları test edilmedi.

## 8. Mekân sayfasında istediğim içerik

Her mekân için hedef:

- Doğru ad, şehir, semt/adres; mümkünse doğrulanmış konum ve şube eşleşmesi.
- Ne yenir: belirli yemek/ürün önerisi ve bunun kaynağı.
- Neden tercih edilir: kısa ve somut gerekçe.
- Gitmeden bil: doğrulanabildiğinde fiyat/bütçe, saat, sıra/rezervasyon, servis veya deneyim bilgileri; tarihleriyle.
- Kaynağı belli puan ve değerlendirmeler; editör görüşünden ayrı.
- Varsa resmî site ve Instagram hesabına yönlendirme.
- **3–5 gerçek fotoğraf**: yemek, ortam ve işe yarayan ayrıntılar. Sayıyı doldurmak için sahte veya ilgisiz fotoğraf yok.
- **2–3 ilgili YouTube videosu**: doğru mekân/şube, anlamlı içerik, sayfa içinde oynatma ve gerektiğinde dış bağlantı.
- Kaynak ve son kontrol zamanı; bilinmeyen bilgiyi kötü özellik gibi göstermeyen tasarım.

Instagram’dan fotoğraf toplama ihtimalini konuşmuştuk; uygulanmış bir yöntem veya sınırsız indirme izni değil. Sosyal hesap bağlantısı, resmî embed ve dosyayı indirip tekrar yayımlamak ayrı seçenekler. Kaynağın görünür olması kullanım hakkı bulunduğu anlamına gelmez.

Google Places olası sağlayıcı. Doğru işletme/şube eşleşmesi, istenen alanlar, güncel ücret/kota/saklama/atıf koşulları incelenmeli. API anahtarı ve faturalandırma açılmış değil. API’nin döndürdüğü yorumlar platformdaki bütün yorumlar sayılmamalı. Puan, değerlendirme sayısı ve gözlem tarihi birlikte düşünülmeli.

YouTube için ilgili videoyu bulmak ile gömülebilirliğini doğrulamak ayrı. Mevcut şemadaki genel `rights_status` alanı tek başına gömme uygunluğunu modellemek için yeterli olmayabilir. Bunu tasarım kusuru olarak incele; kendi medyamız, lisanslı görsel ve sağlayıcı embed’inin kurallarını aynı kefeye koyma.

Bir alan eksik diye bütün sayfayı boş kutularla doldurmak istemiyorum. Eksik içerik UX’ini öner; kullanıcıya hangi gerçek bilgiyle yine de fayda sunulabileceğini açıkla.

## 9. Veri modelinin mevcut hâli ve beklenen gelişimi

Tek esas dosya `dataset.json`. Şehir dosyaları bundan üretilen görünümler. Mekân kimliği UUID; ad/adres düzeltmesinde değişmemeli. Her fiziksel şube ayrı kayıt olarak ele alınmalı. Benzer adlar tek başına birleştirme kanıtı değil.

Mevcut üst yapı `meta`, `cities`, `venues`.

Bir mekânın mevcut alanları:

```text
venue_id, city_id, name, brand_id
address: raw, district, neighborhood, postal_code
coordinates
operating_status, publication_status
source_records[]
external_places[], websites[], social_accounts[]
ratings[], dishes[], photos[], videos[], editorial_notes[]
enrichment
```

`source_records` ham ad/adres, kaynak liste/şehir URL’si, sayfa, kart sırası, gözlem tarihi, eski kimlik, detay/harita URL’si ve kalite notlarını tutuyor. Düzeltilmiş adres orijinal gözlemi silmemeli.

`enrichment` adres/konum, işletme durumu, Google eşleşmesi, site/sosyal hesaplar, puanlar, yemek/editörlük, fotoğraf ve video için ayrı ilerleme durumu tutuyor. `not_started`, bilinmeyen, bulunamadı, başarısız ve tamamlandı anlamları birbirine karıştırılmamalı.

Zenginleştirme kayıtlarında kaynağın URL’si, gözlem zamanı ve doğrulama durumu düşünülmüş. Puanlarda sağlayıcı, değer, ölçek ve yorum sayısı; editör notlarında tür/metin/yazar; medyada kaynak/hak/atıf alanları var. Boş listeler içerik toplanmış demek değil.

Saatler, tam yorum modeli, etiket ilişkileri ve admin sürümleri henüz mevcut v1 şemaya uygulanmadı. Yeni model önerirken arşivi değiştirmeden taşımayı, şema sürümünü, kimlik korumayı ve doğrulama örneklerini açıkla. Her şeyi tek büyük JSON’a veya tek bir güven puanına sıkıştırma.

## 10. Yönetim paneli ve etiketler

Bu özellik doğrudan benim talebim ve MVP gereksinimi: kod düzenlemeden kayıt eklemek/düzeltmek, fotoğraf yüklemek ve mekânlara birden çok etiket atamak istiyorum.

Planlanan akış:

```text
Yönetici girişi → mekânı bul/ekle → bilgileri düzenle
→ yemek/not/fotoğraf/video/etiket ekle → taslak kaydet
→ ziyaretçi görünümünde önizle → yayımla
```

Ziyaretçi üyeliği ayrı konu; admin girişi zorunlu. İlk aşamada tek yönetici yeterli olabilir. Restoran sahiplerine ayrı hesap açmak henüz kapsamda değil.

Planlanan davranışlar:

- Şehir, ad, yayın durumu ve eksik içeriğe göre arama.
- Kaynak orijinalini koruyarak düzenleme; olası tekrar/şube uyarısı.
- Kalıcı taslak, korunan önizleme ve yayındaki sürümün ayrılması.
- Kapak, sıra, açıklama, alternatif metin ve kullanım durumu olan fotoğraf yönetimi.
- Etiket sözlüğü ve mekâna çoklu atama.
- Hatalı kayıtta formun korunması; iki sekmeden güncellemede sessiz üzerine yazmama.
- Değişiklik geçmişi; eski sürümü yeni taslak olarak getirme.
- Yayından kaldırma ile işletmenin kapanmasının ayrı olması.
- Sunucuda yetki kontrolü; özel taslakların ve orijinal medyanın ziyaretçiye sızmaması.

JPEG/PNG/WebP ve dosya başına 10 MB sınırı önceki belgede önerildi; kesin teknik karar veya mevcut uygulama değil. Medya boyutlandırma, EXIF temizliği, depolama, yükleme hataları ve izin geri çekilmesi değerlendirilmeli.

Etiket örnekleri: yemek/mutfak, tek başına yemek, arkadaşlarla, kısa mola, dışarıda oturma, İngilizce menü, vejetaryen seçenek, editör seçkisi. Olgusal etiket ile editoryal değerlendirme ayrılmalı. Fiyat ve “şu an açık” gibi değişken bilgiler tarihsiz etiketlere dönüştürülmemeli.

Ben “yabancıların tercih ettiği mekân” gibi etiketlerden de söz ettim. İngilizce yorum sayısını yabancı ziyaretçi tercihi olarak yorumlamak yeterli değil. Bu etiketin kanıt yöntemi henüz yok. İngilizce menü, bir rehberde yer alma veya editörün ilk kez gelenlere önerisi ayrı iddialar.

Planlanan model `TagDefinition` ve `VenueTagAssignment` ayrımı. Etiket adını değiştirmek kimlik ve ilişkileri bozmamalı. Atamanın gerekçesi, kaynağı ve kontrol tarihi tutulmalı. İç çalışma etiketleri ziyaretçiye gösterilmemeli. Filtreler için aynı grupta VEYA, farklı gruplarda VE önerildi; henüz üretimde uygulanmadı.

## 11. Mimari taslak — kesinleşmiş teknoloji yok

Şu an Python ile üretilen statik HTML/CSS/JavaScript prototipi var. Üretim teknolojisi seçilmedi. Belirli bir framework, veritabanı, kimlik sağlayıcısı veya hosting kullanıldığını varsayma.

Önceki öneri:

```text
Özel kaynak arşivi
  → kontrollü içe aktarım / doğrulama
  → ilişkisel içerik veritabanı
  ↔ giriş korumalı yönetim paneli
  ↔ özel medya deposu / yayımlanabilir türevler
  → önizleme / yayın kontrolü
  → yalnız açık alanlardan oluşan yayımlanmış katalog
  → ziyaretçinin keşif ve mekân sayfaları
```

Tek web uygulaması ve korunan admin alanı önerildi. Hazır CMS ile özel admin karşılaştırması yapılmalı. Taslak/yayın ayrımı, medya yönetimi ve kullanım kolaylığı karar ölçütleri. Mikroservis, ayrı arama kümesi veya ağır altyapı için bugün gösterilmiş bir gerekçe yok.

Mantıksal varlıklar: City, Venue, SourceObservation, ExternalPlace, RatingObservation, Dish, SocialLink, MediaReference/MediaAsset, EditorialNote, TagDefinition, VenueTagAssignment, AdminAccount, ContentRevision, AuditEvent. Bunlar önerilen kavramlar; tümü kurulmuş tablolar değil. User/Favorite ancak ziyaretçi hesap/kaydetme kararıyla eklenmeli.

Arşiv tek doğruluk kaynağı gibi değiştirilmeyecek; canlı editoryal veri ve geçmişi ayrı yönetilecek. Ziyaretçiye iç notlar, taslaklar veya tam ham arşiv gönderilmeyecek. Provider arızası temel keşfi tamamen durdurmamalı; bulunamadı, kota, erişim reddi ve zaman aşımı ayrılmalı.

Senden az sayıda uygulanabilir teknoloji seçeneğini bakım yükü, tek geliştiriciyle ilerleme, admin deneyimi, medya, maliyet ve taşınabilirlik açısından karşılaştırmanı; sonra birini gerekçesiyle önermeni istiyorum. Seçimini benim verilmiş kararım gibi sunma.

## 12. Daha önce bakılan benzer ürünler

Önceki araştırma herkese açık sayfalar ve yardım belgeleriyle sınırlıydı; kapsamlı rakip analizi veya özel panellerin kullanım testi yapılmadı.

| Ürün | Konuşulan fikir | Bizde değerlendirme |
|---|---|---|
| The Infatuation | Kullanım durumları, kısa editoryal gerekçe, “Perfect For” | “Hangi durumda burayı seçerim?” bilgisini güçlendirmek |
| TasteAtlas | Yemekten mekâna keşif | Mekân adını bilmeden “pide yemek istiyorum” diye başlayabilmek |
| HappyCow | Belirli ihtiyaçlara göre filtreler, bilgi/fotoğraf düzenleme | Kontrollü etiketler, yönetilebilir içerik ve ileride düzeltme bildirimi |
| Gastro Obscura / Atlas Obscura | Yerel yemek hikâyeleri ve editoryal seçki | “Bu yeri özel yapan ne?” sorusuna kısa, kaynaklı cevap |

Önceki kaynaklar:

- https://www.theinfatuation.com/new-york/guides/best-hells-kitchen-restaurants
- https://www.tasteatlas.com/best/dishes
- https://www.happycow.net/mobile/android
- https://www.happycow.net/business/faq
- https://www.atlasobscura.com/faq

Gastro Obscura ile Atlas Obscura’nın katkı modellerinin aynı olduğu varsayılmamalı. Yeni analizde güncel gözlemi yeniden doğrula; gördüğün özellik ile kendi önerini ayrı yaz. Tasarım veya içerikleri birebir kopyalamayı önermiyorum.

## 13. Michelin, rota ve daha sonraki fikirler

### Michelin

Merakım yerel listemizin Michelin ile ne kadar kesiştiği ve anlamlı bir fark varsa bunu pazarlamada anlatıp anlatamayacağımızdı. Yıldız alanlar, diğer rehber kategorileri ve geçmiş yıllarda yer alanları birbirine karıştırmamak gerektiğini konuştuk. Gerçek kategori tanımlarını ve güncel sayıları kaynaktan doğrulamak gerekir.

İstanbul’da 80’den fazla olabileceğini düşündüm; **bu doğrulanmış sayı değil**. Elimizde tamamlanmış Michelin veri seti veya hesaplanmış kesişim oranı bulunduğu varsayılmamalı. Ayrı bir Michelin sekmesi yalnız fikir; MVP’nin odağı değil. Önceki asistanın “ayrı bilgi katmanı” önerisi de bağlayıcı bir ürün kararı değil.

### Gastronomi rotası

Gelecekte kullanıcı “İstanbul’da 08.00–20.00 arasında beş duraklık yemek günü istiyorum” diyebilir. Başlangıç/bitiş, ulaşım, tercihler, tempo, çalışma saatleri ve gerçek yolculuk süreleriyle rota düşünülmüştü. İleride yakın tarihî/kültürel noktalar eklenebilir.

Haritada sokakları takip ederek yürüyen 2D karakter fikri de vardı. PostGIS’in kuş uçuşu mesafesi gerçek yürüme rotası değildir; güzergâh geometrisi, süre ve dönüş bilgileri için uygun routing verisi gerekir. Routing sağlayıcısı seçilmedi, animasyon yapılmadı.

**Bunlar sonraki fazlar. VoiceMap, sesli tur ve gelişmiş rotayı şu an bırakıp MVP’ye dönmek istediğimi açıkça söyledim.** Analiz bunları tekrar ilk sürümün merkezine koymamalı.

## 14. Monetizasyon beklentisi

Gelir modeli bulmak istiyorum, fakat şu ana kadar seçilmiş veya doğrulanmış bir model yok. Bu konu önceki çalışmada yeterince geliştirilmedi.

Aşağıdakiler kabul edilmiş ürün kararları değil; senden araştırıp karşılaştırmanı istediğim adaylar:

- Açıkça etiketlenmiş sponsorluk ve seçki iş birlikleri.
- Uygun hizmetlerde rezervasyon/yönlendirme ortaklığı.
- Gerçek ek değer varsa ücretli şehir rehberi veya premium özellikler.
- Yerel işletmelere sunulabilecek hizmetler; kullanıcı önerileriyle çıkar çatışması yaratmadan.
- Reklamın erken aşamada getireceği gelir ile deneyime maliyeti.

Her model için kim öder, neye öder, ne kadar trafik veya içerik kalitesi gerekir, neyi ölçerek test ederiz, işletme/ödeme/moderasyon yükü nedir ve güveni nasıl etkiler sorularını cevapla. Kaynaksız gelir tahmini üretme. Ücretli sıralama ile bağımsız tavsiyeyi gizlice karıştıran model önermemelisin. Gelir için temel karar deneyimini gereksiz yere kısıtlama.

## 15. Mevcut proje planı ve backlog

Belgelerde şu aşamalar var: ürün kararları → içerik/UX keşfi → tıklanabilir prototip → teknik temel → uçtan uca MVP → kapalı beta → portföy/tanıtım.

Yayın tarihi veya haftalık kapasite kesinleşmedi. İçerik araştırmasını kimin yapacağı ve kayıt başına süresi bilinmiyor. Takvim verirken varsayım kullan; yazılım emeği ile içerik üretimini ayrı hesapla. Küçük bir örneklemde araştırma süresini ölçüp genişleme hesabı yapmak önerildi.

Mevcut 28 işin kısa özeti aşağıda. Bunlar **iş listesi**, tamamlanmış özellikler değil. P0/P1 önceki belgenin öncelikleri; yeni analizde sorgulanabilir.

| ID | Öncelik | İş |
|---|---|---|
| GD-001 | P0 | Hedef kullanıcı, şehir, dil ve MVP sınırları |
| GD-002 | P0 | Repo hedefi ve veri sınırı — repo açıldı, ilk commit/push yok |
| GD-003 | P0 | Pilot içeriği seçme, araştırma, kaynak ve süre kaydı |
| GD-004 | P0 | Keşif, filtre, detay ve geri dönüş akışı |
| GD-005 | P0 | Aynı içerikle iki görsel yön |
| GD-006 | P0 | Prototipte görev bazlı kullanıcı gözlemleri |
| GD-007 | P0 | Mimari, sağlayıcı, bütçe ve karar kayıtları |
| GD-008 | P0 | Veri sözleşmesi ve hatalı veri kontrolleri |
| GD-009 | P0 | Taslak/iç bilgi sızdırmayan yayın çıktısı |
| GD-010 | P0 | Keşif ve filtre uygulaması |
| GD-011 | P0 | Gerçek içerikli mekân detayı |
| GD-012 | P0 | İçerik düzeltme ve sürümden geri alma süreci |
| GD-013 | P0 | Ziyaretçi/admin beta doğrulaması |
| GD-014 | P1 | Gerçek sonuçlarla portföy vaka çalışması |
| GD-015 | P0 | Yönetici girişi ve sunucu yetkileri |
| GD-016 | P0 | Mekân listesi, ekleme/düzenleme formu |
| GD-017 | P0 | Fotoğraf/video yönetimi |
| GD-018 | P0 | Etiket sözlüğü ve çoklu atama |
| GD-019 | P0 | Taslak, önizleme, yayın ve geçmiş |
| GD-020 | P1 | Temalı seçkiler ve kısa yerel hikâyeler |
| GD-021 | P0 | Yemek kaydı ve yemekten mekâna keşif |
| GD-022 | P0 | Etiket filtreleri |
| GD-023 | P1 | Bilgi düzeltme bildirimi ve inceleme kuyruğu |
| GD-024 | P1 | Sonra gitmek üzere kaydetme denemesi |
| GD-025 | P1 | Ziyaretçi popülerliği etiketinin kanıt yöntemi |
| GD-026 | P0 | Doğru sosyal hesap ve ilgili video doğrulaması |
| GD-027 | P0 | Google Places eşleştirme ve sunucu entegrasyonu |
| GD-028 | P0 | Dolu/eksik/hatalı puan, yorum ve medya akışları |

Eski teslim planı admin geliştirmesini öne alıyordu; son eleştiri içerik ve ziyaretçinin karar deneyiminin ispatını öne çıkardı. Bu gerilimi çöz: yönetim ihtiyacını ihmal etmeden hangi küçük uçtan uca teslim gerçek değeri en erken gösterir?

Google entegrasyonunun eski belgede P0 olması erişim ve bütçenin onaylandığı anlamına gelmez. Google olmadan ilk içerik kanıtı üretilebiliyorsa bunu açık bir alternatif olarak değerlendir; konuşulan puan/yorum ihtiyacını sessizce kapsamdan çıkarma.

## 16. Belge envanteri

Yerel `proje/docs/` altında şu belgeler var:

1. `01-urun-kapsami.md`: problem, hedef, önerilen MVP, başarı ölçütleri.
2. `02-ux-plani.md`: araştırma, karar akışı, görsel yön ve ekran durumları.
3. `03-sistem-tasarimi.md`: önerilen mimari, veri ilişkileri ve teknik sınırlar.
4. `04-veri-icerik.md`: araştırma, eşleştirme, kaynak ve içerik yönetimi.
5. `05-teslim-plani.md`: aşamalar, bağımlılıklar, 28 iş.
6. `06-kararlar-riskler.md`: kararlar, varsayımlar, açık sorular ve riskler.
7. `07-kalite-portfoy.md`: doğrulama ve portföy yaklaşımı.
8. `08-ilk-iterasyon.md`: ilk prototip ve test notları.
9. `09-benzer-urunler.md`: rakip gözlemleri ve önerilen özellikler.
10. `10-yonetim-paneli.md`: admin akışları ve kabul ölçütleri.
11. `11-etiketler.md`: sözlük, atama, kanıt ve filtre kuralları.
12. `12-mekan-detayi.md`: sosyal/video/Google alanları ve eksik entegrasyonlar.

Belgelerin varlığı kararların onaylandığı veya yazılımın çalıştığı anlamına gelmez. Bazı eski planlar son ürün eleştirisinden önce yazıldı. Güncel ihtiyaçla çelişen yerleri korumak zorunda değilsin; değişiklik önerisini gerekçelendir.

## 17. Başarı ve kabul ölçütleri

Önceki öneri: Beş hedef kullanıcıdan en az dördü yönlendirme almadan üç dakika içinde iki aday bulup birini gerekçesiyle seçebilsin. Bu **test edilmemiş bir başlangıç hedefi**; araştırmayla değişebilir.

Senden bunu geliştirmene ek olarak şu gözlenebilir sonuçları kullanmanı istiyorum:

- Kullanıcı “burada ne yerim ve neden giderim?” sorularına ek araştırma yapmadan makul bir cevap bulabiliyor mu?
- İki aday arasındaki farkı kendi sözleriyle açıklayabiliyor mu?
- Sağlayıcı puanı, editör yorumu ve bilinmeyen alanı ayırabiliyor mu?
- Dar ekranda seçim, detay, geri dönüş ve harita aksiyonu çalışıyor mu?
- Gerçek video oynuyor mu; kapanınca duruyor mu; oynatılamıyorsa çıkış yolu var mı?
- Yönetici bir mekânı düzenleyip fotoğraf/etiket ekleyerek önizleyip yayımlayabiliyor mu?
- Taslak değişikliği yayındaki sürümü hemen bozmuyor mu?
- Yanlış şube, eski bilgi, medya hatası ve sonuçsuz arama anlaşılır biçimde ele alınıyor mu?
- Bir kaydı araştırma, doğrulama ve güncelleme maliyeti sürdürülebilir mi?

Harita tıklaması gerçek ziyaret veya memnuniyet kanıtı değildir. Arayüz testleri kullanıcı araştırması değildir. Yeni ölçüt önerirken neyi ölçtüğünü ve neyi kanıtlamadığını belirt.

## 18. Çalışma ve portföy tercihlerim

Profesyonel bir proje gibi ilerlemek istiyorum; fakat doküman üretimi ürün üretiminin yerine geçmemeli. İşler küçük, görülebilir teslimlere ayrılmalı. Her işin kullanıcı ihtiyacı, bağımlılığı ve denenebilir kabul ölçütü olsun.

Belgeler ve kodlar insan yazmış gibi doğal, anlaşılır olmalı. Doğal görünmek için sahte kişisel deneyim, kusur veya yapılmamış kullanıcı araştırması eklenmemeli. Portföyde gerçek katkılar, karar gerekçeleri, karşılaşılan sorunlar ve doğrulanmış sonuçlar anlatılmalı.

Mevcut çalışan davranışlar ve kaynak arşivi korunmalı. Önerilen büyük değişiklik mevcut sürümün üzerine sessizce yazılmamalı. Gerçek katalog ve özel bilgiler public repoya taşınmamalı. Yayın, commit/push, ücretli servis veya erişim değişikliği ayrı açık yetki gerektirir. Analiz sırasında gereksiz onay sorularıyla ilerlemeyi durdurma.

## 19. Açık konular

- İlk hedef kullanıcı: şehirde yaşayanlar, ziyaretçiler veya ikisinin belirli bir alt grubu?
- İlk yayın kapsamı ve yeterli içerik eşiği: kaç mekân, hangi bölgeler?
- Marka adı nihai mi; beğendiğim görsel referanslar neler?
- Yalnız Türkçe mi; çok dil ne zaman gerekli?
- İçerik araştırması/editörlük ve düzenli güncellemeden kim sorumlu?
- Haftalık zaman, ekip kapasitesi, aylık servis bütçesi ve hedef tarih?
- Hazır CMS mi özel admin mi; üretim teknoloji seçimi?
- Google erişimi ve maliyet modeli; gerçek fotoğrafların kaynağı ve yayın yöntemi?
- Favori/kaydetme için ilk aşamada hesap gerekiyor mu?
- Bağımsız özel yedek nerede tutulacak?
- Gelir modeli hangi kullanıcı değerinden sonra test edilecek?

Bunların hepsini bir kerede soru listesi olarak bana geri gönderme. Analiz için gerçekten belirleyici olanları seç; geri kalanına geri alınabilir öneri sun.

## 20. Cevabını nasıl hazırlamalısın?

Şu sırayla, birbirini tekrar etmeyen bir analiz hazırla:

1. **Dürüst teşhis:** Bugünkü yaklaşım neden kaynak listeden yeterince farklılaşmıyor? En önemli üç sorun ne?
2. **Net ürün önerisi:** İlk kullanıcı, onun karar anı, ürün vaadi ve üç somut kullanım senaryosu. Hangi kısmın benim talebim, hangi kısmın senin önerin olduğunu belirt.
3. **Gerçek içerikli UX taslağı:** Mobil keşif → adaylar → mekân detayı → seçim akışını ekran ve içerik hiyerarşisiyle anlat. Bir dolu, bir eksik kayıt ve sonuçsuz aramayı ele al. Renk/font listesinden ibaret kalma. Örnek mekân bilgisi kullanırsan araştır; araştırmadan ürettiğin metni gerçek olgu gibi sunma.
4. **İçerik edinme planı:** Önce 3–5 kayıtta değer ispatı, sonra İstanbul’daki 235 kayıt, daha sonra diğer şehirler için araştırma/eşleştirme/güncelleme yöntemi. 3–5 fotoğraf ve 2–3 video hedeflerinin bulunabilirlik ve bakım maliyetini sorgula. Otomatik yapılabilecek iş ile editör değerlendirmesini ayır.
5. **MVP kapsamı:** Şimdi / sonra / vazgeç başlıklarında gerekçeli ve sınırlı öneri. Admin ihtiyacını ve asıl karar deneyimini birlikte karşıla. Mevcut 28 işi gerekirse birleştir veya yeniden sırala.
6. **Teknik çözüm:** Az sayıda seçenek, önerilen mimari, veri modeli değişiklikleri, arşivden aktarım, yayın/medya yetkileri ve sağlayıcı hataları. Sadece gerekli teknik ayrıntıları ver.
7. **Monetizasyon değerlendirmesi:** Seçenekleri kullanıcı değeri, güven, trafik gereksinimi, operasyon ve küçük test açısından karşılaştır. Erken aşama için bir öneri ver; gerekirse şu an gelirden önce doğrulanması gerekeni söyle.
8. **Teslim programı:** İlk somut teslim ve sonraki birkaç aşama. Her biri için çıktı, bağımlılık, tahmin varsayımı ve bitirme ölçütü. Henüz kapasite bilinmediği için kesin tarih uydurma.
9. **Portföy yaklaşımı:** Neleri dürüstçe gösterebiliriz, neleri henüz iddia edemeyiz?
10. **En fazla beş kritik soru ve önerilen sonraki adım.** Cevaplanmış konuları yeniden sorma. Sonraki adım gerçek bir karar veya görülebilir ürün çıktısı üretsin.

Önceki çalışmayı savunmak zorunda değilsin. İyi bir fikrin zayıf uygulanmış olabileceğini, bazı özelliklerin gereksiz olabileceğini ve içerik işinin yazılımdan daha zor çıkabileceğini açıkça tartış. Amacın beni ikna etmek değil, doğru ürünü ve uygulanabilir yolu bulmama yardım etmek.
