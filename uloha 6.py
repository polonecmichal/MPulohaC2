# Naprogramuj funkciu, ktorá pre dané x z intervalu <1,20> bude 
#počítať funkčné hodnoty podľa predpisu y= (x**2-1)/(x-3)
for x in range(1, 21):
    if x == 3:
        print(f"x={x} y=nedefinované")
    else:
        y = (x**2 - 1) / (x - 3)
        print(f"x={x} y={y}")