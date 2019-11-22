from veiculo import Veiculo
from combustivel import Combustivel
from calculadora import Calculadora


def main():
    print(
        """
            Esta aplicação tem como finalidade demonstrar os valores que serão gastos
            com combustível durante uma viagem, com base no consumo do seu veículo, e
            com a distância determinada por você!
        """
    )
    print("Os combustíveis disponíveis para este cálculo são:")
    print("    ° Álcool")
    print("    ° Díesel")
    print("    ° Gasolina")

    print(" ")

    comb1 = Combustivel("Gasolina", 4.80)
    comb2 = Combustivel("Álcool", 3.80)
    comb3 = Combustivel("Díesel", 3.90)

    calc = Calculadora()

    try:
        comb1 = Combustivel("Gasolina", 4.80)
        comb2 = Combustivel("Álcool", 3.80)
        comb3 = Combustivel("Díesel", 3.90)
        veiculo = Veiculo(
            input("Distância em Quilometros a ser percorrida: "),
            input("Consumo de combustível do veículo(km por lt)")
        )
        print("""
                O valor gasto será de:
                Gasolina: R$ {}
                Álcool:   R$ {}
                Díesel:   R$ {}
            """.format(
            calc.calcular_valor_gasto_combustivel(veiculo, comb1),
            calc.calcular_valor_gasto_combustivel(veiculo, comb2),
            calc.calcular_valor_gasto_combustivel(veiculo, comb3))
        )
    except ValueError:
        print("o valor não é válido!")




if __name__ == '__main__':
    main()