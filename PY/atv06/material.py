"""
    Eu ainda não entendi dicionários, então esse arquivo
    é deticado preenchimento a essa lacuna que tá vazia
"""

user_dic = {
    # chave : #valor

    "user":"eu mesmo",
    "email":"alguum@email.com",
    "senha":123,
    "CPF":999999999-21,
    "ativo":True,
    "endereco":[
            {
                "rua":"16",
                "cidade":"taguatinga",
                "estado":"Df"
            }
        ]
} 

print(user_dic,type(user_dic))

for i in range(0,1):
    print(user_dic["user"])
    print(user_dic["email"])
    print(user_dic["senha"])
    print(user_dic["CPF"])
    print(user_dic["ativo"])
    print(user_dic["endereco"])

# METODOS PARA DICIONARIO
# len - QUANTAS CHAVES EXISTEM NO DICIONARIO
# keys - RETORNA AS CHAVES
# values - RETORNA OS VALORES
# items - RETORNA CHAVES E VALORES
# setdefault - ADICIONA VALOR SE A CHAVE NÃO EXISTE
# get - BUSCA CHAVE
# pop - APAGA UMA CHAVE ESPECÍFICA (del)
# popitem - APAGA A ULTIMA CHAVE
# update - ATUALIZA UM DICIONARIO

print(len(user_dic))
print(list(user_dic.keys()))
print(list(user_dic.values()))
print(list(user_dic.items()))

user_dic.setdefault('saldo', 0)
print(user_dic)

print(user_dic.get('nome'))

user_dic.pop('nome')
print(user_dic)

user_dic.popitem()
print(user_dic)

user_dic.update({
    'nome' : 'Victor',
    'email' : 'victor.rohod@docente.senai.br'
})

print(user_dic)

    