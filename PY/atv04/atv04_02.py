# lista
num_lista=[]
num_maior = 0

# Adicionando a Lista (a)

for i in range(0,4):

    num_add = int(input(f'Digite o {i+1}º numero >> ')) 

    num_lista.append(num_add)

print(num_lista)

# verificando o maior (b)
for i in range(0,4):
    if num_lista[i] > num_maior:
        num_maior = num_lista[i] 

print(num_maior)

