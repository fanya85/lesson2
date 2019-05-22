"""

Домашнее задание №1
Условный оператор: Сравнение строк
* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты
"""
one = input()
two = input()


def main(one, two):


    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if one.isdigit() is False and two.isdigit() is False:
        if one == two:
            return 1
        elif len(one) > len(two):
            return 2
        elif two == "learn":
            return 3
        else:
            return 666
    else:
        return 0


if __name__ == "__main__":
    a = main(one, two)
print(a)