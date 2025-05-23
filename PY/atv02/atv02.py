from datetime import datetime as dt

anoT = dt.now().year

print(anoT)

ano = int(input("Digite seu ano de nascimento >> "))

print(f"Sua idade é {int(anoT) - ano}")