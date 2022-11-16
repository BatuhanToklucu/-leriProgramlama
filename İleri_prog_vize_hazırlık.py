#Elamanları klavyeden girilen dizini ortalamasını bulan program.

list=[]
#list =list()

elemansayisi=int(input("Eleman giriniz"))

toplam=0
for i in range(0, elemansayisi):
    eleman=int(input("Eleman giriniz"))
    list.append(eleman)
    #list.insert(i,eleman)
    #toplam=toplam+eleman


for i in range(0,elemansayisi):
    toplam=toplam+list[1]

ortalama=toplam/elemansayisi

for i in range(0,elemansayisi):
    if list[i]>ortalama:
        sayac=sayac+1
        print(list[1])


# Elamanları klavyeden girilen dizini ortalamasını bulan program'ın ortalamadan yüksek olanları başka dizine atama.

list=[]
#list =list()

elemansayisi=int(input("elman giriniz"))

toplam=0
for i in range(0, elemansayisi):
    eleman=int(input("eleman giriniz"))
    list.append(eleman)
    #list.insert(i,eleman)
    #toplam=toplam+eleman


for i in range(0,elemansayisi):
    toplam=toplam+list[1]

ortalama=toplam/elemansayisi
list2=[]

for i in range(0,elemansayisi):
    if list[i]>ortalama:
        sayac=sayac+1
        print(list[1])
        list2.append(list[i])

print(sayac, "adet sayı ortalamanın üzerindedir. ")
print(list2)


#Klavyeden girilen boyutların eşit olup olmadıklarını bulan program.

list=[]
list2=[]

boyut=int(input("Liste boyutunu giriniz"))

for i in range(0,boyut):
    eleman=int(input("1.liste elemanı giriniz"))
    list.append(eleman)


for i in range(0,boyut):
    eleman=int(input("2.liste elemanı giriniz"))
    list2.append(eleman)

esitMi=True

for i in range(0,boyut):
    if list[i]!=list2[i]:
        esitMi=False
        break

print(list)
print(list2)
if esitMi:
    print("iki liste eşittir. ")
else:
    print("iki liste eşit değildir. ")



#klavyeden girilen sayının tam bölenlerini ekrana yazdıran program.

Sayi=int(input("Sayı giriniz"))

for i in range(1,Sayi+1):
    if Sayi%i==0:
       print(i)

        