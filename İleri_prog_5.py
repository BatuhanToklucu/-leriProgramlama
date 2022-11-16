#Eleman sayısını klavyeden girilen program
list=[]

elemansayisi=int(input("Elememan sayısını giriniz"))

for i in range(0,elemansayisi):
    eleman=input(i,"elemanı girin")
    list.append(eleman)

print("List =",list)


#Eleman sayısını klavyeden girilen program ve elemanların toplamını diziye atayan program.

list=[]

elemansayisi=int(input("Elememan sayısını giriniz"))
toplam=0
for i in range(0,elemansayisi):
    eleman=int(input("Elemanı giriniz"))
    list.append(eleman)
    toplam=toplam+eleman

print("List =",list)
print("Eleman Toplamı",toplam)


# 0 ile 100 arasında rastgele olacak şekilde 10 oluşurup bu sayıları bir liste içerisine aktaran,
# yine bu liste içerisindeki sayıların kaç tanesinin 50'den küçük olduğunu ekrana yazdıran program.

import random 

list=[]

for i in range(0,10):
     sayi=random.randint(0,100)
     list.append(sayi)

for i in range(0,10):
    if list[1]<50:
        count=count+1

print("50'den küçük eleman sayısı =",count)
print(list)            

