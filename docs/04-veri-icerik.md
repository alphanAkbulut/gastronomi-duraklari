# Veri ve içerik operasyonu

## Veri varlığı

21 şehirde 1.118 kayıt; İstanbul 235. Tüm kayıtların ad ve ham adresi var; 29 harita URL'si eksik. İlçe, koordinat, gerçek işletme eşleştirmesi, puan, sosyal hesap ve medya araştırması tamamlanmış değildir. Kaynakta bir bozuk URL ve farklı işletmelerce paylaşılan bir harita URL'si grubu önceki kalite raporunda işaretlidir. Bu kayıtlar otomatik düzeltilmez veya birleştirilmez.

## Önerilen pilot

İstanbul’dan 20 kayıtlık pilot seçildi; 16 kayıt yerel prototipte, dört kayıt inceleme listesinde. İçerik araştırması henüz tamamlanmadı. Farklı yemek türleri, bölgeler ve mevcut içerik kalitesi temsil edilsin; yalnızca en çok fotoğrafı bulunan yerler seçilmesin. Her kayıt için harcanan gerçek süre ve eksik alanlar ölçülsün. 235 kayıt içindeki kalan araştırma işinin takvimi bu pilotun sonucuna göre hesaplanır.

## Kayıt başına kontrol sırası

1. Ad, adres, şehir ve şube eşleşmesi; kaynaklar çelişirse inceleme kaydı.
2. Harita hedefi ve varsa sağlayıcı işletme kimliği; isim benzerliği tek başına yeterli değildir.
3. Resmî site ve sosyal hesapların aynı işletmeye ait olduğunu doğrulama.
4. Ne yenir, neden gidilir ve önemli koşullar için kaynaklı metin; ziyaret yapılmadıysa ziyaret yorumu yazmama.
5. Varsa puan, ölçek, yorum sayısı ve gözlem zamanı; sağlayıcı şartlarını doğrulama.
6. 3–5 gerçek fotoğraf ve 2–3 ilgili video kullanıcı talebindeki hedef içeriktir. Bunlar her mekân için mevcut veya kullanılabilir varsayılmaz; eksikliği açıkça tutulur. Medyanın aynı şubeye ait olması ve gösterim izni/uygunluğu kontrol edilir.
7. Mobil detay sayfasında önizleme ve yayın kararı.

## Veri durumları

`not_started`: araştırılmadı. `in_progress`: çalışılıyor. `verified`: araştırma konusu gerekli kanıtla kontrol edildi. `not_found`: arandı, bulunamadı; tarih ve kapsam notu gerekir. `needs_review`: çelişki veya şüphe var. `failed`: işlem başarısız; yokluk kanıtı değildir.

Yayınlanmış kayıt açık işletme anlamına otomatik gelmez. “Şu an açık” gibi iddialar güncel ve yeterli veri olmadan gösterilmez. Kaynağın listesinden kalkma, işletmenin kapandığı anlamına gelmez.

## Yayın için önerilen asgari eşik

Ad/şube ve adres kontrol edilmiş; kaynak ve kontrol tarihi var; kullanıcıyı yanlış işletmeye yönlendirecek açık çelişki yok; gösterilen her medya ve puanın kullanım biçimi kontrol edilmiş. Ne yenir/neden gidilir içeriği kanıtla desteklenmiş. Eksik medya tek başına sahte medya üretme gerekçesi değildir. Eksik içerikli kayıtların katalogda görünüp görünmeyeceği ürün sahibince pilot sonunda kararlaştırılır.

## Özel arşiv ve açık ürün ayrımı

Ham kaynak ve iç kontrol notları özel kalır. Sitenin ziyaretçisi yayımladığımız alanları görebilir; webde gösterilen bilgi için gizlilik sözü verilemez. Repo private olsa bile açık sitenin içerikleri açık olur. Veri toplamak, sağlayıcı fotoğrafı/yorumunu sınırsız saklama veya yeniden yayımlama izni anlamına gelmez. Instagram scraping yöntemi ve Google/YouTube saklama-gösterim şartları onaylanmış entegrasyon sayılmaz; gerçek yöntem seçilirken güncel kaynaklar incelenir.

## Güncelleme ve korunma

İlk aktarım sabittir; düzeltmeler yeni gözlem/güncelleme olarak işlenir. Alan değeriyle birlikte kaynak ve tarih korunur. Eşleştirme kararı geri izlenebilir olmalıdır. Yinelenen kayıt birleştirmesinde eski kimlikten yeni kimliğe yönlendirme kaydı tutulması önerilir.

Yerel kopya ve ZIP aynı bilgisayarda olduğu için cihaz kaybına karşı bağımsız yedek değildir. İkinci, özel yedek hedefi ayrıca seçilecek; bu projede bir bulut yüklemesi yapılmamıştır. Yedek, geri yükleme denemesiyle doğrulanır.

## Panelle içerik hazırlamak

Kaynak gözlemleri salt okunur kalacak. Panelde yapılan düzeltme, kaynak değerinin üstüne yazmak yerine düzenlenmiş bir içerik sürümü oluşturacak. Fotoğraflar dosya deposunda; açıklama, kullanım bilgisi, kapak ve sıra veritabanında tutulacak. Etiketler [ortak sözlükten](11-etiketler.md) seçilecek.

“Kaydet” taslak oluşturur; “Yayımla” kontrol edilmiş sürümü ziyaretçiye açar. Medya kullanımı belirsizse taslak saklanabilir ama o medya yayımlanmaz. Başlangıç JSON dosyalarına bu aşamada etiket veya medya eklemedik; model geçişi uygulama iş listesinde.
