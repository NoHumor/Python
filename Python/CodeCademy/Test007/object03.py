from Test007.object02 import get_float as взять
from Test007.object02 import calc as посчитать
from Test007.object02 import output as брякнуть

брякнуть("Это простейший калькулятор. Для выхода наберите выход.")

while True:
    а = взять("введите первую переменную")
    while type(а) != float:
        брякнуть("Данные не верны.")
        а = взять("введите целое или дробное число")

    б = взять("введите вторую переменную")
    while type(б) != float:
        брякнуть("Данные не верны.")
        б = взять("введите целое или дробное число")

    операция = взять("введите операцию")
    while not операция:
        брякнуть("Не существует такой операции.")
        операция = взять("введите верную операцию (/ * + -)")

    try:
        брякнуть(посчитать(а, б, операция))
    except ZeroDivisionError:
        брякнуть("бесконечность")

    брякнуть("")
