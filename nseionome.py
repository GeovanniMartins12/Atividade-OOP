class Pessoa:

    def __init__(self, idade, nome):
        self.nome = nome
        self.idade = idade

    def imprimir_dados(self):
        print('Alguns dados ai')

class Medico(Pessoa):

    def imprimir_crm(self):
        print('123456789')


class Paciente(Pessoa):

    def imprimir_sintomas(self):
        print('Dor, pedra nos rins, cancer')

pessoa = Pessoa('Jubiscleudo', 980)
pessoa.imprimir_dados()