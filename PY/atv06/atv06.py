"""
Programa que cadastra e armazena produtos

Deve incluir:{
    "nome": "nome"<-String,
    "estoque" : "estoque"<-int,
    "preco" : "preco"<- float lol
}


1 - Cadastro de Produto Você precisa criar um programa que armazene informações de um produto em um dicionário.
As informações devem incluir nome, preço e quantidade em estoque. 
Depois, o programa deve exibir todas as informações do produto.
"""

produto_dic = {
    "nome": [],
    "estoque": [],
    "preco": []
}

print("1 - cadastro\n2 - sair")
opcao = int(input(">>> "))


match opcao:
    case 1:
        print("*"*4,"Cadastro","*"*4)
        nome_dic = str(input("Nome >> "))
        
        estoque_dic = int(input("Estoque >> ")) 
        
        preco_dic = float(input("Estoque >> "))

        produto_dic["nome"].append(nome_dic)

        produto_dic["estoque"].append(estoque_dic)

        produto_dic["preco"].append(preco_dic)

        print(produto_dic)

        for i in produto_dic:
            print(f'Nome do produto: {produto_dic["nome"][i]}\nEstoque: {produto_dic["estoque"][i]}\nPreco: {produto_dic["preco"][i]}')
    case 2:
        print("Programa encerrado") 
         