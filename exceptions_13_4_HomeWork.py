try:
    # Из условия задачи я не понял, можем ли мы использовать подключаемые библиотеки и циклы,
    # # поэтому предлагаю выбрать тот вариант, который больше походит под условия задания
    select_metod = input("""Выберете метод, по которому надо решить задание:
    1 - метод с использованием бибилиотеки Numpy
    2 - метод ручного перебора вариантов
    3 - метод с использованием цикла
    ввод номера метода:  """)
    int_metod = int(select_metod)
except ValueError as e:
    print("Вы допустили ошибку при выборе варианта,\nкод ошибки:  ", e)
else:
    per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
    stavki = list(map(float, per_cent.values()))
    if int_metod == 1:
        import numpy
        money = int(input("Какую суммы Вы готовы разместить на депозит в предложенных банках?  "))
        stavka = numpy.array(stavki) * money / 100
        print("deposit = ", stavka)
        deposit = int(stavka.max())
        print("Максимальная сумма, которую вы можете заработать — %d рублей за год" % (deposit))
    elif int_metod == 2:
        money = int(input("Какую суммы Вы готовы разместить на депозит в предложенных банках?  "))
        tkb = round(float(stavki[0]) * money / 100)
        skb = round(float(stavki[1]) * money / 100)
        vtb = round(float(stavki[2]) * money / 100)
        sber = round(float(stavki[3]) * money / 100)
        deposit = [tkb, skb, vtb, sber]
        print("deposit = ", deposit)
        m_deposit = max(deposit)
        print("Максимальная сумма, которую вы можете заработать — %d рублей за год" % (m_deposit))
    elif int_metod == 3:
        money = int(input("Какую суммы Вы готовы разместить на депозит в предложенных банках?  "))
        i_max = len(stavki)
        deposit = []
        for i in range(0, i_max):
            deposit.append(round(float(stavki[i]) * money / 100))
        print("deposit = ", deposit)
        m_deposit = max(deposit)
        print("Максимальная сумма, которую вы можете заработать — %d рублей за год" % (m_deposit))
    else:
        print("Вы выбрали неверное значение. Прочитайте условие ещё раз.")
finally:
    print("Программа завершила расчёт")