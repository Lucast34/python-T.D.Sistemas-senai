# input

print("O valor deve ter . em vez de ,")

peso = float(input("Digite o peso >> "))


if peso <= 50:
    print("Não houve excesso")
else:
    # tirando a sobra com peso excedido
    peso =  peso - 50

    resultado_multa = 4.00 * peso 

    print("ACIMA DO PESO!!\nA multa foi de: R$",resultado_multa)
