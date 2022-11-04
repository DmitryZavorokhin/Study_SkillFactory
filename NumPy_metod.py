per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Какую суммы Вы готовы разместить на депозит в предложенных банках?  "))
stavki = (list(map(float,per_cent.values())))
tkb = round(float(stavki[0])*money/100)
skb = round(float(stavki[1])*money/100)
vtb = round(float(stavki[2])*money/100)
sber = round(float(stavki[3])*money/100)
deposit =[tkb, skb, vtb, sber]
print("deposit = ", deposit)
m_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать — %d рублей за год" % (m_deposit))