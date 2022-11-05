#1-10 arası sayıların toplamı

toplam=0
for i in range(0,11):
    toplam=toplam+1

print(toplam)


#1-10 arası tek sayıların toplamı

toplam=0
for i in range(0,11):
    if i%2==1:
        toplam=toplam+i

print(toplam)

#1-10 arası tek sayıların toplamı(while hali)
i=0
toplam=0
while i<11:                   # 11i dahil etmek için küçüktür işareti eşittir koyulur
    toplam=toplam+i
    i=i+1                      #sonsuz dögüyü engeller
print(toplam)    


#faktoriel hesaplama
sayi=int(input('sayı giriniz: '))
carpim=1  
for i in range (1,sayi+1):
    carpim=carpim*i
print(carpim)

#faktoriel hesaplama (while hali)
sayi=int(input('sayı giriniz'))
carpim=1
while sayi>0:
    carpim=carpim*sayi
    sayi=sayi-1                     #sonsuz döngüyü kırar
print(carpim)    

#Toplamda 10 sorunun sorulduğu bir sınavda her doğru cevap için 10 puan alınırken her yanlış cevap için -5 puan alınmaktadır.
#Tüm soruları cevaplayan bir kişinin doğru yanlış sayısı klavyeden girildiğinde toplam puanını ekrana yazan programın kodunu yazınız.

dogruSayisi=int(input('doğru sayısını giriniz'))
yanlisSayisi=int(input('yanlis sayi giriniz'))

dogruPuan=0
yanlisPuan=0
toplamPuan=0

toplamSoru=dogruSayisi+yanlisSayisi

if toplamSoru==10:
    dogruPuan=dogruSayisi*10
    yanlisPuan=yanlisSayisi*-5
    toplamPuan=yanlisPuan+dogruPuan
    print('Toplampuanınız =',toplamPuan)
else:
    print('Soru sayinizi kontol edin')    


