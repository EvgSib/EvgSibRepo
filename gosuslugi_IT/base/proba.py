# -*- coding: utf-8 -*-
'''
Анна,Математика,85;Анна,Химия,90;Борис,Математика,75;Борис,История,80;Евгений,Математика,95;Евгений,История,85
Математика,80;Химия,60;История,80
'''

def find_students_without_debt(student_grades_str, passing_grades_str):
    # 1. Парсим проходные баллы
    passing_grades = {}
    for item in passing_grades_str.split(';'):
        if item:
            course, score = item.split(',')
            passing_grades[course] = int(score)

    # 2. Парсим оценки студентов и группируем по студентам
    student_data = {}
    for item in student_grades_str.split(';'):
        if item:
            name, course, grade = item.split(',')
            if name not in student_data:
                student_data[name] = {}
            student_data[name][course] = int(grade)

    # 3. Определяем студентов без задолженностей
    students_without_debt = []
    for name, grades in student_data.items():
        is_clear = True
        for course, grade in grades.items():
            if grade <= passing_grades[course]:
                is_clear = False
                break
        if is_clear:
            students_without_debt.append(name)

    # 4. Выводим результат
    if not students_without_debt:
        return "Пусто"
    else:
        return "\n".join(sorted(students_without_debt))

# Пример использования
student_grades = "Анна,Математика,85;Анна,Химия,90;Борис,Математика,75;Борис,История,80;Евгений,Математика,95;Евгений,История,85"
passing_grades = "Математика,80;Химия,60;История,80"

result = find_students_without_debt(student_grades, passing_grades)
print(result)


