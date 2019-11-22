class Combustivel:
    __nome: str
    __preco: float

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @nome.setter
    def nome(self, nome):
        self.__nome = str(nome)

    @preco.setter
    def preco(self, preco):
        self.__preco = float(preco)
