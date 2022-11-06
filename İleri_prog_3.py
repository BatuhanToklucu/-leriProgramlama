#Final ve vize notunu hesaplayan program

vize=int(input("vize notu"))
final=int(input("final notu"))

ortalama=(vize*0.4)+(final*0.6)

if ortalama>40:
    print("geçtiniz")
else: print("kaldınız")



#Klavyeden girilen taban ve üs değerine göre o sayının üssünü hesaplayan ve sonucu ekrana yazdıran program

Taban=int(input("klavyeden sayı giriniz"))
Üs=int(input("üs değeri giriniz"))

carpim=1
for i in range(0,Üs):
    carpim=carpim*Taban

print(Taban,"'in",Üs,"inci kuvveti =",carpim)

#import math                                                         #kütüphaneli kullanımı
#print(int(math.pow(2,5)))



# Sıfır girilinceye kadar klavyeden tam sayı değerleri alın,bu sayılardan en büyüğü ile en küçüğü bulan ve ekrana yazdıran program

sifirMi=True
eb=0
ek=0
while sifirMi:

    sayi=int(input("bir sayı giriniz"))
    if sayi==0:
        break
    else:
        if sayi>eb:
            eb=sayi
        elif sayi<ek:
            ek=sayi    

print("En büyük",eb)
print("En küçük",ek)



# Bir mülakatta katılımcının başarılı olabilmesi için İngilizce ya da Fransızcadan birini bilmesi ve yaşının 40'tan küçük olması gerekmektedir.
#Katılımcının yukarıdaki bilgileri, adunu ve soyadını sorarak mülakat sonucunu "Başarılı" ya da "Başarısız" çıktıları ile gösteriniz.

ad_soyad=input("Adınızı ve Soyadınızı girin")
yas=int(input("yaşınızı giriniz"))
if yas>40:
    print("yaş sınırını aştınız.")
    print("mülakat başarısız")
else:
    cevap=input("İngilizce ve ya Fransızca biliyor musun? E/H")
    if cevap=="H":
        print("Dil şarını sağlayamıyorsunuz")
        print("Mülakat başarısız")
    elif cevap=="E":
        print("Tebrikler", ad_soyad, "Mülakat başarılı")
    else: print("Yanlış giriş")   



# Klavyeden girilen ilk metin içinden, ilk metin'de olan ama ikinci metinde olmayan öğeleri yazdıran program.

metin1=input("1. metni girin")
metin2=input("2. metni girin")

for i in metin1:
    if i not in metin2:
        print(1)

