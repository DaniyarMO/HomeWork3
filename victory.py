import random
famous_people = {
    'Валерий Харламов': '14.01.1948',
    'Борис Ельцин': '01.02.1931',
    'Михаил Горбачев': '02.03.1931',
    'Николай Гоголь': '01.04.1809',
    'Михаил Булгаков': '15.05.1891',
    'Александр Пушкин': '06.06.1799',
    'Нурсултан Назарбаев': '06.07.1940',
    'Георгий Данелия': '25.08.1930',
    'Лев Толстой': '09.09.1828',
    'Михаил Лермонтов': '15.10.1814'
}
random_people = random.sample(list(famous_people.items()),5)
correct_answer = 0
incorrect_answer = 0
print("Угадайте даты рождения следующий знаменитых людей (вводит дату в формате 'dd.mm.yyyy')")
for person, date in random_people:
    user_input = input(f"дата рождения {person}: ")
    if user_input == date:
        print("Правильно!")
        correct_answer += 1
    else:
        write_date = date.split('.')
        month = {'01':'январь', '02':'февраль', '03':'март', '04':'апрель', '05':'май', '06':'июнь', '07':'июль', '08':'август', '09':'сентябрь', '10':'октябрь', '11':'ноябрь', '12':'декабрь'}
        date_text = f"{int(write_date[0]):d} {month[write_date[1]]} {write_date[2]} года"
        print(f"Неверно. Правильный ответ: {date_text}")
        incorrect_answer += 1

print("\nРезультаты:")
print("Правильные ответы:", correct_answer)
print("Неправильные ответы:", incorrect_answer)
test = str(input("Хотите начать с начала? (да/нет) "))
if test.lower() == "нет":
    print("Спасибо за игру!")

