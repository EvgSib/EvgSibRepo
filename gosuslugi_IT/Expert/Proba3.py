# -*- coding: utf-8 -*-
students_info = 'Анна,Математика,75;Анна,Химия,70;Борис,Математика,75;Борис,История,80;Евгений,Математика,50;Евгений,История,75 '
scores_info = 'Математика,80;Химия,60;История,80'

students = {}

for item in students_info.split(';'):
    name, course, grade = item.split(',')
    if name not in students:
        students[name] = {}
    students[name][course] = int(grade)

