nominal = int(input("Введите количество элементов: "))
number = []
numbers = []
for i in range(nominal):
    number = int(input("введите число: "))
    numbers.append(number)
numbers.sort()
print(numbers)

