class Veiculo:
    __consumo: float
    __distancia: float

    def __init__(self, distancia, consumo):
        self.distancia = distancia
        self.consumo = consumo

    @property
    def consumo(self):
        return self.__consumo

    @property
    def distancia(self):
        return self.__distancia

    @consumo.setter
    def consumo(self, consumo):
        self.__consumo = float(consumo)


    @distancia.setter
    def distancia(self, distancia):
        self.__distancia = float(distancia)

