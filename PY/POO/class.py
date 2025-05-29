# como vimos em Poo.py isso é uma declaração de uma classe

class Cachorro:
    # atributo
    especie = "Canino"


    def __init__(self, nome, idade):
        # atributo com instacial (Uma maneira burra de traduzir instance atribute)
        self.nome = nome # <- gera uma copia desse atributo, quando ele for modificado somento ele vai ser afetado
        self.idade = idade 

