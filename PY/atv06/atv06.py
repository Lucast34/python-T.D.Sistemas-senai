"""
Programa que cadastra e armazena produtos

Deve incluir:{
    "nome": "nome"<-String,
    "estoque" : "estoque"<-int,
    "preco" : "preco"<- float lol


}

"""



produto_dic={
    "nome" : None,
    "estoque" : 0,
    "preco": 0.0
}


while True:

    decisao = int(input("Escolha >> "))

    match decisao:
        case 1:
            print("placeholder add")
            break
        case 2:
            print("placeholder update")
            break
        case _:
            print("invalide input")

    decisao = int(input("Escolha pra continuar >>"))

    if(decisao == 1):print("passou")
    else: break

