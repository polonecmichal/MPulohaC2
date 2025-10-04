#Naprogramuj funkciu , ktorá sčíta dokopy čísla od 1 do N.
a = 0
n = int(input("zadaj n:"))
for i in range( 0 , n + 1):
    a += i
print(a)