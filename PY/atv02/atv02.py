from datetime import datetime as dt

anoT = dt.now()

anoF= anoT.year

print(anoF)

ano = int(input("Digite seu ano de nascimento >> "))

print(f"Sua idade é {anoF - ano}")