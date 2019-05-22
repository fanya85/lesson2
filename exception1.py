"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    d = {"Как дела?": "Спасибо, хорошо", "Что делаешь?": "Учусь программировать"}
    try:
        while True:
            vopros = input("Спроси меня: ")
            if vopros in d:
                print(d[vopros])
            else:
                print("Введите ответ на вопрос", vopros)
                d[vopros] = input()
    except KeyboardInterrupt:
        print("Пока!")
	    
    
if __name__ == "__main__":
    ask_user()