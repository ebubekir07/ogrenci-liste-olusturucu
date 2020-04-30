# ogrenci-liste-olusturucu
v1.0 : Ad,soyad,sınıf,numara içerir. Veri getirme,silme,ekleme bulunur.

v2.0 : Ad,soyad,sınıf,numara,şube,tc,telefon,doğum tarihi içerir. Ekleme penceresi ayrı açılır.

v3.0 : Ad,soyad,sınıf,numara,şube,tc,telefon,doğum tarihi içerir. Ekleme penceresi ayrı açılır.
Şifre korumalıdır. İlk kullanımda şifreyi kendi oluşturur ilk şifresi "admin"dir.
şifre ve kullanıcı adı "veritabanı.db" dosyasında saklanır. Şifre ve kullanıcı adı değiştirilebilir ve eklenebilir.
İki adat yetki seviyesi bulunur. Seviye "1":yönetici seviyesidir öğrenci ekleme,silme yetkisi vardır.
Seviye "2":normal kullanıcı seviyesidir öğrenci verilerini görebilir silemez,ekleyemez.

v4.0 : versiyon 3 e ek olarak not bilgisi girme eklendi. öğrencinin bölümüne göre notlar girilir. Ortalaması belge 
durumu ve belgeleri kaç puan ile kaçırdığı hesaplanır. Yetki seviyesi 2 olan kullanıcılar, not ekleme ve öğrenme yapabilir.
Program içerisinde oturum kapatılabilir.

NOT: Programı nerede çalıştırırsanız veritabanı oraya kurulur.Veritabanını taşırsanız tekrar kurulur.
programı rar dan çıkartmadan çalıştırırsanız rar ın bulunduğu klasöre veritabanını kurar.
