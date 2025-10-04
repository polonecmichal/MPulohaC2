# Naprogramuj program, ktorá vypíše čísla od 1 po N a ich druhé mocniny. Pričom N je argumentom programu
n = int(input("Zadaj číslo N: "))
k = int(input("Zadaj číslo K: "))
for i in range(n, k + 1):
    print(f"{i} {i**2}")