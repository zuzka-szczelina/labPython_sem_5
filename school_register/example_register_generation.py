import random
import datetime
import json
from copy import copy


def student_generator(number_of_students): #no repetitions
    names = ['Ann', 'Mark', 'Tom', 'Jane', 'Tina', 'Julia', 'Victoria']
    surnames = ['Smith', 'Brown', 'Johnson', 'Walker', 'Gray', 'Turner']
    student_list = []
    i = 1
    while i <= number_of_students:
        next_student = {'name': random.choice(names), 'surname': random.choice(surnames)}
        if all(next_student != s for s in student_list):
            student_list.append(next_student)
            i += 1
        else:
            continue
    return student_list

def generate_score(number_of_grades, student_list):
    grades = [2, 3, 4, 5]
    student_score = []
    for student in student_list:
        student_score = random.choices(grades, k=number_of_grades)
        student.update({'score': student_score})

def class_date_generator( start_year, start_month, start_day , step, number_of_lessons):
    step = datetime.timedelta(days=step)
    start_date = datetime.date(start_year, start_month, start_day)
    date = start_date
    date_list = []
    i=1
    while i <= number_of_lessons:
        date_list.append(date.isoformat())
        date += step
        i += 1
    return date_list

def generate_attendance(date_list, student_list):
    present_absent = [1,0]
    present_possibility = 0.7
    weights = [present_possibility, 1-present_possibility]
    for student in student_list:
        student_attendance = {}
        for date in date_list:
            student_attendance.update({'{}'.format(date): random.choices(present_absent, weights=weights)[0]})
        student.update({'attendance': student_attendance})

#tu poniżej jest funkcja, chciałam zrobić tak żeby tworzyła od razu zmienną o zadanej nazwie
#czy to się tak robi? (zmienna powstaje ale podkreśla na czerwono z dopiskiem "unresoved reference nazwa_zmiennej")
#odp: tak to jest git
def generate_school_class2(name, dates, students):
        globals()[name] = {'name': name, 'dates': dates, 'students': students}

# tu jest wersja która działa, ale trzeba przypisać wynik do nazwy,
# a chciałabym wiedzieć jak wprowadzać nazwę jako argument funkcji
def generate_school_class(name, dates, students):
    school_class = {'name': name, 'dates': dates, 'students': students}
    return school_class


student_list = student_generator(12)
print("student list:\n{}".format(json.dumps(student_list, indent=2)))

math_dates = class_date_generator(2023, 2, 13, 7, 5)
physics_dates = class_date_generator(2023, 2, 14, 7, 6)
programming_dates = class_date_generator(2023, 2, 16, 7, 7)

math_students = [copy(s) for s in random.sample(student_list, 5)]
physics_students = [copy(s) for s in random.sample(student_list, 7)]
programming_students = [copy(s) for s in student_list]
print("math students:\n{}".format(json.dumps(math_students, indent=2)))

generate_attendance(math_dates[:-1], math_students)
generate_attendance(physics_dates[:-2], physics_students)
generate_attendance(programming_dates[:-3], programming_students)

generate_score(3, math_students)
generate_score(3, physics_students)
generate_score(3, programming_students)
print("attendance and score generated:\n{}".format(json.dumps(math_students, indent=2)))

#generate_school_class2('math', math_dates, math_students)
math = generate_school_class('math', math_dates, math_students)
physics = generate_school_class('physics', physics_dates, physics_students)
programming = generate_school_class('programming', programming_dates, programming_students)
print("math class:{}".format(json.dumps(math, indent=2)))

school_register = {'year_name': '3b', 'students': student_list, 'classes': {'math': math, 'physics': physics, 'programming': programming}}

with open('register.json', 'w') as f:
    json.dump(school_register, f, indent=2)
