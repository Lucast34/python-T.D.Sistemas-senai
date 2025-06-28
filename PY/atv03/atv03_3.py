#variavel 

num_maior = 0

# loop 
# refatorado

for i in range(0,3):
    num = int(input("Digite um numero: "))
    if num_maior < num: num_maior = num

print("Numero maior: ",num_maior)