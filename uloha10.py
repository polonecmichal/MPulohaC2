#vypíš čísla od 1-N odzadu, za sebou.
n = int(input("Zadaj číslo N: "))
numbers=""
for i in range(n, 0, -1):
    numbers+=str(i)+" "
print(numbers)