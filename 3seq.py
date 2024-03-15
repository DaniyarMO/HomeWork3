#Запрашиваем необходимое количество элементов для ввода
while True:
    nominal1 = int(input("Введите количество элементов первого списка: "))
    nominal2 = int(input("Введите количество элементов второго списка: "))
    #Если он не совподают, просим снова ввести
    if nominal1 != nominal2:
        print("Необходимо ввести одинаковое количество элементов")
    else:
        break
#Создаем пустые переменные
number_one = []
number_two = []
for i in range(nominal1):
#Просим ввести элементы первого списка
    number = []
    number = (input("Введите числа первого списка: "))
    number_one.append(number)
for i in range(nominal2):
#Просим ввести элементы первого списка
    number = []
    number = (input("Введите числа второго списка: "))
    number_two.append(number)
#Сравниваем элементы двух списков
result = list(set(number_one) - set(number_two)) + list(set(number_two) - set(number_one))
print("Ваши числа первого списка: ", number_one)
print("Ваши числа второго списка: ", number_two)
print("Результат: ", result)


