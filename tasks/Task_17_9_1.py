import random
posledovatelnost = []
indexes =[]
# spisok_str = input("Введите последовательность целых чисел через пробел: ")
# spisok_str ="1 2 2 2 2 2 6 4 5"
#spisok_str ="79 68 21 0 74 95 0 9 64 3 "
spisok_str =""
k=0
dlina = random.randrange(5,50)

while k<dlina: #  формирование списка из чисел и преобразование строку( по условиям задачи) и обратное преобразование в список
    d = random.randrange(0,100)
    k += 1
    spisok_str = spisok_str + str(d) + " "
posledovatelnost = list(map(int,spisok_str.split()))
max_num = max(posledovatelnost)
min_num = min(posledovatelnost)
min_num_1 = min_num
print(posledovatelnost)
poisk_min_dubl = posledovatelnost.count(min_num) # проверка того, что минимальное значение в списке одно
if poisk_min_dubl == 1: # если минимальное значение одно, то чтоб указать индекс значения менее вводимого пользователем нужно, чтоб вводимое число было более минимального значения.
    min_num_1 = min_num +1 # о чём и сообщаем пользователю

try:
    print(f'Число от {min_num_1} до {max_num}')
    element = int(input("Вводите здесь: ")) #Сообщение № 1
    poisk_element_dubl = posledovatelnost.count(element)  # проверка повторения введенного значения в списке
    if poisk_min_dubl > 1 and min_num == element:
        print(c)  # Сообщение № 3( если минимальный элемент списка повторяется и он введен пользователем)
    if max_num == min_num:
        print(c) #Сообщение № 3
    if max_num < element or (min_num_1) > element:
        a = element/0 #Сообщение № 2
except ValueError: #Сообщение № 1
    print("Вы ввели не число.")
except ZeroDivisionError: #Сообщение № 2
     print("Вы ввели число, выходящее за значения чисел в списке.")
except NameError: ##Сообщение № 3: Обработка ошибки, массив состоит только из одинаковых чисел и поэтому возможен сбой в поиске
     print("Массив состоит только из одинаковых чисел или введенное число соответствует первому элементу в списке и повторяется, и поиск будет некорректен,\nпоскольку в задании не сказано, как обрабатывать такой сценарий, то это ошибка")
else:
    def sort(posledovatelnost):
        for i in range(1, len(posledovatelnost)):
            x = posledovatelnost[i]
            idx = i
            while idx > 0 and posledovatelnost[idx - 1] > x:
                posledovatelnost[idx] = posledovatelnost[idx - 1]
                idx -= 1
            posledovatelnost[idx] = x
        return posledovatelnost
    print(f'array = {sort(posledovatelnost)}')
    # for i in range(len(posledovatelnost)): # вывод в консоль список индексов
    #     indexes.append(i)
    # print(f'indexes={indexes}')

    def binary_search(array, element, left, right):
        middle = (right + left) // 2  # находим середину

        if left > right:  # если левая граница превысила правую,
            return f'Номер предыдущего элемента: index ={middle} со значением {posledovatelnost[middle]}\nНомер равного или большего элемента: index ={middle+1} со значением {posledovatelnost[middle+1]}'

        if array[middle] == element:  # если элемент в середине,
            if poisk_element_dubl > 1:
                return binary_search(array, element, left, middle-1)
            else:
                return f'Номер предыдущего элемента: index= {middle-1} со значением {posledovatelnost[middle-1]}\nНомер равного или большего элемента: index= {middle} со значением {posledovatelnost[middle]}'
        elif element < array[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
            return binary_search(array, element, left, middle - 1)
        else:  # иначе в правой
            return binary_search(array, element, middle + 1, right)
    print(binary_search(posledovatelnost, element, 0, len(posledovatelnost)))





