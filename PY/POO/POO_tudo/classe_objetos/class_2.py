class Carro:
    def __init__(self,nome,modelo,tipo,motor):
        self.nome = nome
        self.modelo = modelo
        self.tipo = tipo
        self.motor = motor

class Dono:
    def __init__(self,pnome,fullnome):
        # os self(objetos) não é obrigado a serem iguais aos parametros, porem as instancias(atributos) precisam ser 
        # os atributos do  python deve ser minusculos e separados por underscore  "_"
        self.nome = pnome
        self.nomeInt = fullnome
        # porém e melhor deixar tudo igual, nesse exemplo deixei diferente para mostrar que funciona mesmo assim.

nova_pessoa = Dono("João","Augusto")

print(nova_pessoa)
print(type(nova_pessoa))
print(nova_pessoa.nome)
print(nova_pessoa.nomeInt)
