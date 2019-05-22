"""
Домашнее задание №1
Цикл for: Оценки
* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

school_scores = [{'school_class': '4a', 'scores': [3,4,4,4,4,5,2]}, {'school_class': '5a', 'scores': [3,4,2,5,3,5,2]}, {'school_class': '6a', 'scores': [3,4,5,5,5,4,5,2]}]

def main():
    t=0
    s=0
    for i in school_scores:
        for v in i['scores']:
            t += sum(i['scores'])
            s += len(i['scores'])        
    print("Средний балл по школе:", t // s)
        
        
    for i in school_scores:
        for v in i['scores']:
            t = sum(i['scores'])//len(i['scores'])
        print("Средний балл", i['school_class'],":",t)
    
if __name__ == "__main__":
    main()