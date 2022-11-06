# Klavyeden girilen bir şifrenin karakterlerini kontrol ederek girilen şifrenin 4 karakter olana kadar yeni şifre isteyen, 
# girilincede de doğru şifreyi ekranda gösteren program.

Sifre=input("Şifre giriniz")

uzunluk=len(Sifre)
Kontrol=True
while Kontrol:
    if uzunluk==4:
        print("Şifrniz oluşturuldu")
        Kontrol=False                                     #break yerine kullanıldı break ile aynı görevi yapıyor
    else:
        Sifre=input("Şifrenizi yeniden giriniz")



# Bir otoparkın ücret tarifesi aşağıdaki gibidir.
#1 saate kadar 5TL
#1.5 saat arası: saat başı 4tl
#5 saatten fazla: saat başı 3 tl
#Buna göre kullanıcının girdiği otoparkta kalınan saat süresine göre ödenecek miktarı bularak ekrana yazdırınız.

kalinan_saat=int(input("Kaldığınız saati giriniz"))
toplam_ücret=0
if kalinan_saat<=1:
    toplam_ücret=5
elif (kalinan_saat>1) and (kalinan_saat<=5):
    toplam_ücret=kalinan_saat*4   
elif kalinan_saat>5:
    toplam_ücret=kalinan_saat*3

print("Ödeyeceğiniz miktar =",toplam_ücret)  



#Parola girilirken Türkçe karakter uyarısı veren program.

kontol=True
turkce_karakter="ığüşöçĞÜİÖÇ"

while kontol:
    sifre=input("Şifrenizi giriniz")
    for i in sifre:
        if i in turkce_karakter:
            print("Şifrede Türkçe karakter olamaz")
        else:
            print("Şifreniz oluşturuldu")
            kontol=False                                              #kontrol burada break yerine kullanıldı
