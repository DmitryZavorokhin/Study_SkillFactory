import numpy
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Какую суммы Вы готовы разместить на депозит в предложенных банках?  "))
stavki = list(map(float,per_cent.values()))
stavka = numpy.array(stavki)*money/100
print("deposit = ", stavka)
deposit = int(stavka.max())
print("Максимальная сумма, которую вы можете заработать — %d рублей за год" % (deposit))

