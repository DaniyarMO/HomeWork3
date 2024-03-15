nominal = int(input("Введите количество элементов: "))
number = []
numbers = []
for i in range(nominal):
    number = int(input("введите число: "))
    numbers.append(number)
    number_set = set(numbers)
print(';'.join(map(str, number_set)))