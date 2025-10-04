#naprogramuj funkciu, ktorá sčíta všetky párne čísla od 1-N
n = int(input("zadaj n:"))
a = 0
for i in range(1, n):
    if i % 2 == 0:
        a += i
print(a)