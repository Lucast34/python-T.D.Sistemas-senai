# input

idade = int(input("Digite o sua idade >> "))


# Estrutura de decisão
if idade <= 0:
    print("Valor invalido")
else:
    if(idade > 0 and idade < 15):print("Criança")

    if(idade >= 15 and idade < 30):print("Jovem")

    if(idade >= 30 and idade < 60):print("Adulto")
    
    if(idade >= 60):print("Idoso")
