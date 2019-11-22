class Calculadora:
    __combustivel_gasto: float
    __valor_total_gasto: float

    def calcular_valor_gasto_combustivel(self, veiculo, combustivel):
        if veiculo.consumo <= 0 or veiculo.distancia <= 0:
            raise Exception('o valor recebido não pode ser menor ou igual a zero')

        self.__combustivel_gasto = veiculo.distancia/veiculo.consumo
        self.__valor_total_gasto = round(self.__combustivel_gasto*combustivel.preco, 2)
        return self.__valor_total_gasto
