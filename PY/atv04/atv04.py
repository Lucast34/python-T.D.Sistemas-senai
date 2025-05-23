# variavel
multa = 4.0

# input

print("O valor deve ter . em vez de ,")

peso = float(input("Digite o peso >> "))

print(peso)


if peso < 50:
    print("Não houve excesso")
else:
    peso = 50 - peso

    resultado_multa = peso/multa

    print("")
