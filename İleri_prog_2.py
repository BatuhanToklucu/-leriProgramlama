# Klavyeden 0 girilene kadar pozitif ve negatif sayılar girilecek.
#Girilen sayıların kaçı negatif? kaçı pozitif? Sayıların ortalaması 

sifirMi=True
negaSayac=0
pozSayac=0
toplam=0

while sifirMi:
     Sayi=int(input('klavyeden sayı giriniz'))
     if Sayi ==0:
        break
     elif Sayi<0:
        toplam+=toplam+pozSayac
        negaSayac=negaSayac+1
     else:
        toplam=toplam+pozSayac
        pozSayac=pozSayac+1
ort=toplam/(pozSayac+negaSayac)
print("Ortalama", ort)


# 3 basamaklı sayıların basamak toplamını yazdıran program

Sayi=int(input("3 basamaklı sayı giriniz"))
birler=Sayi%10
yuzler=(int)(Sayi/100)
onlar1=int(Sayi/10) 
onlar=onlar1%10

print("yüzler",yuzler, "onlar",onlar,"Birler",birler)
toplam=yuzler+onlar+birler
print("Toplam =",toplam)


# Toplamda 3 cevap hakkı verilen bir sayı tahmin oyununda:
# Yarışmacı sayıyı doğru tahmin ettiğinde kaçıncı hakkında doğru tahmin ettiği ile birlikte ekrana yazan ve programı sonlandıran,
# (Örnek Çıktı: 2. Tahminde bildiniz).
# 3 hakkında da doğru tahmin edemeyen yarışmacıya “Doğru tahmin yapamadınız” mesajı veren programın kodunu yazınız.

import random

sayi=random.randint(0,100)                     #randint int fonksiyon atar       #range fonk. sonuncu dahil değildir

for i in range(0,3):
    tahmin=int(input("Tahmin giriniz"))
    if sayi==tahmin:
        print("Tebrikler bildiniz")
        break  
    else:
        print("Bir daha deneyiniz")



# Klavyeden girilen sayının asal olup olmadığını bulan uygulamayı yazınız

Sayi=int(input("Sayı giriniz"))
    
for i in range (2,Sayi):
    if sayi%i==0:
        print("Asal değildir")
    else:
        print("Sayı asaldır")



#Klavyeden girilen bir kelime içindeki sesli harfleri bulan program yazınız

kelime="klavyeden girilen bir kelime içindeki sesli harfleri bulma"
sayac=0
harf=input("Aranacak harfi giriniz")
for i in kelime:
    if i==harf:
        sayac=sayac+1

print(harf," Harfi cümle içinde" ,sayac,"tane var")        


#Klavyeden girilen bir kelime içindeki sessiz harfleri bulan program yazınız

cumle="klavyeden girilen bir kelime içindeki sesli harfleri bulma"
sesli='aıoueiöü'
sessiz='qwrtypğsdghjklşzxcvbnmç'
harfler_sesli=" "
harfler_sessiz=" "

for i in cumle:
    if i in sesli:
        harfler_sesli=harfler_sesli+i
    elif i in sessiz:
        harfler_sessiz=harfler_sessiz+i    


print("Sesli harfler ", harfler_sesli)
print("Sessiz harfler ",harfler_sessiz)
