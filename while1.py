"""
Домашнее задание №1
Цикл while: ask_user
* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    """
    Замените pass на ваш код
    """
    print("Как дела?")
    x = input()
    while x != "Хорошо":
        print("Это не то, что я хотел услышать!")
        x = input()   

    
if __name__ == "__main__":
    ask_user()