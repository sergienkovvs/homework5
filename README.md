Homework5
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
