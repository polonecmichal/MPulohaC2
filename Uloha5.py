# Naprogramuj program, ktorá vypíše čísla od 1 po N a ich druhé odmocniny. Pričom N je argumentom programu
from math import sqrt
n = int(input("Zadaj číslo N: "))
squareRoot = float(0)
k = int(input("Zadaj číslo K: "))
for i in range(n, k + 1):
    squareRoot = round(sqrt(i),2)
    print(f"{i} - {squareRoot}")
