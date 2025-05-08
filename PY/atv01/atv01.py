NOME = str(input("Digite o seu nome: "))
EMAIL = str(input("Digite o seu email: "))
SENHA = int(input("Digite a sua senha:"))


user = {
    'NOME':NOME,
    'EMAIL':EMAIL,
    'SENHA':SENHA
}

print(f'nome:{user['NOME']}\nemail{user['EMAIL']}\nsenha{user['SENHA']}')

