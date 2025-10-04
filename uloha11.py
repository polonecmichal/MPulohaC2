#Naprogramuj funkciu, ktorá vypíše všetky čísla od 0-N, ktoré sú deliteľné siedmymi a štyrmi.
n = int(input("zadaj n:"))
for i in range(0, n+1):
    if (i%7==0 and i%4==0 and i != 0):
        print(i)