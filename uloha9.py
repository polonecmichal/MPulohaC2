#Vypíš všetky nepárne čísla od z do k (kde z-zaciatok, k - koniec) Napr.pre z=6 a pre k=10 sa vypíše 7,9
z = int(input("Zadaj začiatok: "))
k = int(input("Zadaj koniec: "))
for i in range(z, k + 1):
    if i % 2 != 0:
        print(i)