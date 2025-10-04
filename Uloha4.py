#Naprogramuj program, ktorá vypíše čísla od 1 po N a ich druhé mocniny. Pričom N je argumentom programu
n = int(input("Zadaj číslo N: "))
for i in range(1, n + 1):
    print(f"{i} {i**2}")