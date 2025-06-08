import datetime as dt

class Carro:
    def __init__(self,nome,modelo,tipo,motor):
        self.nome = nome
        self.modelo = modelo
        self.tipo = tipo
        self.motor = motor
    
    # metodo
    def andar(self):
        return f"{self.nome} esta andando.."

class Dono:
    def __init__(self,pnome,fullnome):
        # os self(objetos) não é obrigado a serem iguais aos parametros, porem as instancias(atributos) precisam ser 
        # os atributos do  python deve ser minusculos e separados por underscore  "_"
        self.nome = pnome
        self.nomeInt = fullnome
        # porém e melhor deixar tudo igual, nesse exemplo deixei diferente para mostrar que funciona mesmo assim.

        # Definindo atributos com valores padrões 
        self.date_joined = dt.date.today()
        self.esta_ativo = True

    # metodo
    def mostrar_data(self):
        return f"O usuario {self.nome} entrou no site as {self.date_joined:%d/%m/%y}"

    #metodo
    def ativo_inativo(self, simnao):
        # se for True tem que retornar ativo e se for false tem que retornar inativo
        self.esta_ativo =  simnao

# Criando uma instancia
nova_pessoa = Dono("João","Augusto")

# Printando o resultado para cada atributo da instancia que foi criada
print(nova_pessoa)
print(type(nova_pessoa))
print(nova_pessoa.nome)
print(nova_pessoa.nomeInt)

# mudando o valor do atributo de uma objeto

nova_pessoa.nome = "Paulo"

print(nova_pessoa.nome)

print(nova_pessoa.mostrar_data())

# modificando um atributo do objeto(usando um metodo) 
print(nova_pessoa.esta_ativo)

nova_pessoa.ativo_inativo(False)

print(nova_pessoa.esta_ativo)