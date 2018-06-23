# -*- coding: UTF-8 -*-
from imposto import ISS, ICMS, ICPP, IKCV

class Calculador_de_imposto(object):

    def realizar_calculo(self, orcamento, imposto):

        imposto_calculado = imposto.calcula(orcamento)

        print(imposto_calculado)

"""if __name__ == '__main__':

    from orcamento import Orcamento, Item

    calculador = Calculador_de_imposto()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item - 1', 50))
    orcamento.adiciona_item(Item('Item - 2', 200))
    orcamento.adiciona_item(Item('Item - 3', 250))

    print('ISS e ICMS')
    calculador.realizar_calculo(orcamento, ISS())
    calculador.realizar_calculo(orcamento, ICMS())
    print('ISS com ICMS')
    calculador.realizar_calculo(orcamento, ISS(ICMS()))

    print('ICPP e IKCV')

    calculador.realizar_calculo(orcamento, ICPP())
    calculador.realizar_calculo(orcamento, IKCV())
    print('ICPP com IKCV')
    calculador.realizar_calculo(orcamento, ICPP(IKCV()))"""