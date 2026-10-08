# Kalite, yayın ve portföy

## Doğrulama kapsamı

- Veri: kimlik benzersizliği, şehir referansı, şema ve alanlar arası kurallar, kaynak/tarih; eşleştirme için insan incelemesi.
- Ürün: arama → filtre → detay → geri → harita ana akışı; boş/hata/eksik veri.
- UX: dar/geniş ekran, klavye, görünür odak, okunabilirlik, medya yüklenmediğinde kullanım.
- Entegrasyon: zaman aşımı, kota, erişim reddi, bulunamadı, yanlış şube; gizli anahtarların istemcide bulunmaması.
- Yönetim: taslağın canlıya sızmaması, sunucuda yetki kontrolü, eşzamanlı düzenleme, medya yükleme hatası, etiketin süresi geçmesi ve sürüm geri dönüşü.
- Yayın: yalnız yayımlanmış alanlar, dış linkler, özel veri/anahtar taraması, sürüm geri alma ve yedekten okuma.

Bunlar ürün geliştikçe yapacağımız kontroller. İlk prototipte çalıştırdığımız denemeler [prototip notlarında](08-ilk-iterasyon.md) yer alıyor. `scripts/check_project.py` ise doküman bağlantılarını ve temel dosya yapısını kontrol ediyor; bütün veri şemasını doğrulamıyor.

## Ortamlar ve yayın

Yerel geliştirme → erişimi kontrol edilen inceleme ortamı → onaylanmış canlı sürüm. Önizleme linkinin kendiliğinden özel olduğu varsayılmaz; erişim kısıtı test edilir. Demo yayımlama ve public repo ayrı kararlardır. Ürün sahibi yayın hedefini ve içeriği onaylamadan yayın yapılmaz.

Her teslimde: ne değişti, hangi kabul ölçütü sağlandı, nasıl denendi, bilinen eksik ve geri dönüş yolu. Kritik sorunlar çözülmeden beta genişletilmez. Analitik kullanılacaksa hangi olayların hangi amaçla toplandığı belirlenir; tam adres/konum gibi gereksiz kişisel bilgiler toplanmaz.

## Portföyde bu projeyi nasıl anlatacağız?

1. Problem: dağınık bilgiyle yemek seçimi ve yanlış tercih maliyeti.
2. Rol: ürün sahibinin gerçek katkıları; kullanılan AI desteği; yapılmayan araştırmaları sahiplenmeme.
3. Başlangıç kanıtı: kaynak seçkisi ve eksikleri, gerçek görüşme bulguları varsa anonim özet.
4. Kararlar: neden bu kapsam, neden bu içerik sırası, hangi alternatifler elendi?
5. Tasarım: akışlar, iki yön, test sonrası değişiklikler.
6. Teknik uygulama: gerçek mimari, veri kaynakları ve sınırlar.
7. Sonuç: yalnız ölçülen görev başarısı, performans ve kullanım; tahmin ayrı.
8. Açık noktalar ve sonraki deney.

Portföyde ham özel katalog yerine izinli ürün ekranları ve gerekiyorsa sentetik örnek veri kullanılır. Bakanlık veya Michelin ile resmî ortaklık/teyit iddiası kurulmaz. Repo lisansı kullanıcı kararıdır; varsayılan bir açık kaynak lisansı eklenmemiştir.
