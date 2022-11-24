"""Создайте класс одной из геометрических фигур (например, прямоугольника), где в конструкторе задаются атрибуты:
 начальные координаты x, y, width и height (или другие в зависимости от выбранной фигуры).
Создайте метод, который возвращает атрибуты прямоугольника как строку ( постарайтесь применить магический метод __str__)."""

class Geo:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f'Geo:{self.x},{self.y},{self.width},{self.height}' # вариант 1( как в задании)
    def varr(self):
        return f'Geo:{self.x},{self.y},{self.width},{self.height}' # вариант 2
sq = Geo(10,20,30,40)
print('Результат по заданию № 16.9.1:    ',sq)
print('Результат по заданию № 16.9.1:    ',sq.varr())
"""апишите код для описания геометрической фигуры.
Создайте класс «прямоугольник» с помощью метода init(). На выходе в консоли вам необходимо получить площадь данной фигуры"""

class Pr:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def plo(self):
        return self.a * self.b
ss = Pr(3,2)
print('Результат по заданию № 16.9.2:    ',ss.plo())

"""В проекте «Дом питомца» добавим новую услугу — электронный кошелек. Необходимо создать класс «Клиент», который будет содержать данные о клиентах и их финансовых операциях. О клиенте известна следующая информация: имя, фамилия, город, баланс.
Далее сделайте вывод о клиентах в консоль в формате:
«Иван Петров. Москва. Баланс: 50 руб.»"""

class Clients:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'{self.name} {self.surname}, {self.city}, Баланс: {self.balance} руб.'
    def Spisik_Klientov(self):
        return f'{self.name}, {self.surname}, {self.city}'
client_1 = Clients('Иван',"Петров","Москва",50)
print('Результат по заданию № 16.9.3:    ',client_1)

'''Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов. Вам необходимо написать программу,
 которая позволит составить список гостей. В класс «Клиент» добавьте метод, который будет возвращать информацию только
  об имени, фамилии и городе клиента.
Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.'''

client_2 = Clients('Петя',"Сидоров","Вельск",50000)
client_3 = Clients('Вася',"Попов","Спб",1)
Spisik_Klientov_1 = [client_1,client_2,client_3]
for client in Spisik_Klientov_1:
    print(client.Spisik_Klientov())


