#Написать программу которая получит имя и возраст пользователя,
# проверяет возраст и выдаёт приветственное сообщение в зависимости от возраста:
#  - меньше нуля или ноль или не число: “Ошибка, повторите ввод”;
#  - больше нуля до 10 не включая: “Привет, шкет #Имя#”;
#  - от 10 до 18 включая: “Как жизнь #Имя#?”
#  - больше 18 и меньше 100: “Что желаете #Имя#?”
#  - в противном случае: “#Имя#, вы лжете - в наше время столько не живут...”
# Программу необходимо завернуть в вечный цикл.
# После очередной отработки кода, спрашивать у пользователя "Желаете выйти? (Д/Y)".
# Если ответ будет буква "Д" или буква "Y" в любом регистре, то произвести выход из вечного цикла.
# В противном случае продолжить выполнение программы заново.

age_prompt = "Скількі вам років: "
value_error = "Помилка, спробуйте ще раз"
what_is_your_name = "Як Вас звати: "
out_cycle = "Желаете выйти? "
cycle_out = ["Y", "y", "Д", "д"]
while True:
    age = input(age_prompt)
    name = input(what_is_your_name)
    if not age.isdigit() or int(age) <= 0:
        print(value_error)
    elif int(age) <= 9:
        print("Привет, шкет", name)
    elif int(age) <= 18:
        print("Как жизнь", name, "?")
    elif int(age) < 100:
        print("Что желаете", name,"?")
    else:
        print("вы лжете - в наше время столько не живут", name, "...")
    out = input(out_cycle)
    if out in cycle_out:
        break

