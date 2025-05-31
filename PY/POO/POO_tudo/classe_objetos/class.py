# como vimos em Poo.py isso é uma declaração de uma classe

class Cachorro:
    # atributo
    especie = "Canino"


    def __init__(self, nome, idade):
        # atributo com instacial (Uma maneira burra de traduzir instance atribute)
        self.nome = nome # <- gera uma copia desse atributo, quando ele for modificado somento ele vai ser afetado
        self.idade = idade 

    """
    def __init__(self,nome,idade,cor):
        self.nome = nome
        self.idade = idade
        self.cor = cor
    
    Por enquanto o python não da suporte a mutiplos constructors,
    Porém existe um outra maneira de contornar esse problema. 
    """


# A classe tem que ser declarado em uma variavek
doguinho = Cachorro("menino",14)
doguinho_2 =Cachorro("Luke",11)


print(f'{doguinho.especie}\n{doguinho.nome}\n{doguinho.idade}')

print(f'{doguinho_2.nome}\n{doguinho_2.idade}\nprint passou')


