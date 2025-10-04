#Naprogramuj funkciu, ktorá v intervale od  <začiatok,  koniec>  zistí počet čísel, ktoré sú deliteľné ôsmimi
z = int(input("Zadaj začiatok: "))
k = int(input("Zadaj koniec: "))
counter = 0
for i in range(z, k+1):
    if i%8==0 and i !=0 :
        counter += 1
print(counter)