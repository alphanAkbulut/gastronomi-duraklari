# Etiketler: küçük bir kelime, net bir anlam

Bir mekâna birden çok etiket ekleyebilmelisin. Ama her kayıt için serbestçe yazarsak “tek başına”, “yalnız yemek” ve “solo” kısa sürede üç ayrı filtreye dönüşür. Bu yüzden panelde ortak bir etiket listesi olacak; mekâna buradan seçim yapılacak. Yeni etiket de panelden oluşturulabilecek.

Henüz hiçbir gerçek mekâna aşağıdaki etiketler atanmadı. Bunlar başlangıç sözlüğü ve kullanım kurallarıdır.

## Hangi bilgiyi nasıl tutacağız?

| Grup | Örnek | Nasıl kullanılacak? |
|---|---|---|
| Yemek / mutfak | Pide, döner, Karadeniz mutfağı | Yemek ve mutfak sözlüğüne bağlı; yalnız mekân adından türetilmez |
| Durum / deneyim | Tek başına yemek, arkadaşlarla, kısa mola | Editörün gerekçesiyle; kesin hizmet garantisi gibi sunulmaz |
| Hizmet / fiziksel özellik | İngilizce menü, dışarıda oturma, paket servis | Kaynak veya doğrudan kontrol tarihiyle |
| Beslenme seçeneği | Vejetaryen seçenek, vegan seçenek | Güncel menü/işletme bilgisiyle; alerjen güvenliği garantisi yerine geçmez |
| Editör seçimi | İlk kez gelenlere önerimiz | Kısa gerekçeyle ve editoryal öneri olduğu belirtilerek |
| Popülerlik | Yabancı ziyaretçiler arasında popüler | Ölçüm kapsamı ve kanıt yöntemi belirlenmeden yayımlanmaz |
| İç çalışma durumu | Adres kontrolü gerekli, fotoğraf izni eksik | Yönetici filtresi; kamuya açık etiket sözlüğüne karışmaz |

Fiyat ve çalışma saati tarihli yapılandırılmış alanlardır. “Ucuz” veya “şu an açık” etiketleriyle bunların güncellik sorununu saklamayacağız. Kullanıcıya görünen filtreler yalnız yayımlanmış ve uygun durumdaki bilgilerden oluşur.

## “Yabancıların tercih ettiği” etiketi

Bu fikri iki ayrı ihtiyaç olarak ele almak daha faydalı:

- **Ziyaretçinin işini kolaylaştıran özellik:** İngilizce menü, yabancı dilde rezervasyon bilgisi gibi doğrudan kontrol edilebilir şeyler.
- **Kimler arasında popüler olduğu:** Gerçek tercih hakkında iddia. İngilizce yorum sayısından kişinin yabancı olduğu veya mekânı tercih ettiği sonucunu çıkarmayız. Yorum dili, milliyet ve ziyaret amacı aynı şey değildir.

İlk sürümde ilk grubu destekleyelim. İkinci etiketi sözlükte taslak olarak tutalım. Yayımlamak için hangi kaynağın kullanılacağı, dönem, örneklemin kapsamı ve yorumun sınırı belirlenmeli. Üç yoruma bakıp genel bir popülerlik rozeti vermeyelim. Bir gezi rehberinde yer alıyorsa bunu daha dar biçimde “X rehberinde yer alıyor” olarak kaynaklı göstermek mümkün.

“Kente ilk kez gelenlere önerimiz” ise ayrı bir editör seçkisidir; yabancıların davranışını ölçtüğümüz anlamına gelmez. Hangi ihtiyaca cevap verdiğini kısa metinle açıklarız.

## Sözlük ve mekâna atama ayrı kayıtlar

**Etiket tanımı:** `tag_id`, sabit anahtar, Türkçe ad, grup, açıklama, dahil etme/dışlama kuralı, alternatif adlar, `active/retired/draft` durumu, halka açık mı, filtrede kullanılabilir mi. Görünen ad değişse de kimlik değişmez. Başka dilde adlar gerekirse aynı kimliğe eklenir.

**Mekân etiketi:** `assignment_id`, `venue_id`, `tag_id`, `proposed/verified/disputed/expired` durumu, gerekçe, kanıt türü, kaynak URL'si veya iç kanıt referansı, kontrol eden yönetici, `observed_at`, `review_due_at` ve bağlı içerik sürümü. Durum/hizmet/popülerlik gruplarının kanıt kuralları farklı olabilir; hepsini tek bir güven yüzdesine indirgemiyoruz.

İç kanıt ve kontrol eden hesabın bilgisi herkese gönderilmez. Ziyaretçi yalnız yayımlanmasına karar verilen etiket adı, kısa açıklama ve uygunsa açık kaynak/tarihi görür. “Kaydet” atamayı otomatik yayımlamaz.

## Yönetirken ne olacak?

- Aynı etiketi aynı mekâna iki kez eklemek engellenir.
- Ad değişikliği mekân bağlantılarını bozmaz. Ortak bir etiketin görünür adını değiştirmek bütün kullanım yerlerini etkilediği için önce etkilenen kayıtlar gösterilir ve değişiklik yayımlanır.
- Benzer etiketleri birleştirme sonraya kalabilir; ilk sürümde kullanımdan kaldırma ve yerine önerilen etiketi seçme yeterli.
- Süresi geçen atama inceleme kuyruğuna düşer ve yeniden doğrulanana kadar kamuya açık filtreden/rozetten çıkarılır. Süreler etikete göre belirlenir; örneğin güncel hizmet bilgisi ile tarihsel bir özellik aynı sıklıkta kontrol edilmez.
- Toplu etiketleme sonraki aşama. İlk sürümde tek kayıttan ilerleyip yanlış bilgiyi yüzlerce yere yayma riskini azaltıyoruz.
- Kartta en fazla birkaç karar verdiren etiket gösterilir; geri kalanı detayda bulunur. Bir kartı rozet panosuna çevirmeyelim.

## Filtre davranışı

Aynı gruptaki seçenekler VEYA, farklı gruplar VE ile birleşir: `(pide veya döner) ve dışarıda oturma`. Sonuç sayısı görünür, seçimler tek tek kaldırılabilir. Eksik bilgi, “bu özellik yok” anlamına gelmez. Belirli özellik filtresinde yalnız o özelliği doğrulanmış kayıtların gelmesi ve kapsamın eksik olabileceğinin anlaşılması gerekir.

## Mevcut veriyle geçiş

`lezzet_dataset_v1` ve `venue.schema.json` bu adımda değiştirilmedi. Uygulama geliştirilirken etiketler ayrı tanım/atama tabloları olarak eklenebilir. Eski kayıtlar boş etiket ilişkisiyle içe alınır; bilinmeyen etiketler tahmin edilmez. Yayın API'si ve dışa aktarım şeması sürümlenir; mevcut mekân kimlikleri korunur.

Bu model; etiket ekle/çıkar, yeniden adlandırma, süresi geçme, erişim ve filtre birleşimi örnekleriyle test edilmeden tamamlanmış sayılmayacak.
