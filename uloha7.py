#Naprogramuj funkciu, ktorá vypíše všetky čísla od 1-N, ktoré sú deliteľné troma.
n = int(input("Zadaj číslo N: "))
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)