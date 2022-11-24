# рекурсия( сумма чисел от 1 до n)
def sum(n):
    if n == 1:
        return 1
    return n+(n-1)
#print(sum(2))
# с помощью рекурсивной функции развернуть строку
def raz(m):
    mn = len(m)
    if mn == 0:
        return ''
    else:
        return m[-1] + raz(m[:-1])
#print(raz('китнаморенеромантик'))

# вычисление суммы цифр числа( например, 123  - 6) только с помощью рекурсии( без циклов,строк, списков и массивов)
def sumN(k):
    if k < 10:
        return k
    else:
        return k % 10 + sumN(k // 10)
print(sumN(100000))