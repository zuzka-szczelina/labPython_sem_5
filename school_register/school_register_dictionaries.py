import random
import datetime


#info dla ziomka z labów:
#these are auxiliary functions for me to generate data
#so I assume they do not count towards method limit (max 8)
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

#tu nie wiem czy potrzebnie robię słownik (dodaję datę do obecności)
#bo wszystkie daty w które mają być zajęcia są już i tak jako osobna lista
# ale tak jest chyba czytelniej i widać które zajęcia już były :/
def generate_attendance(date_list, student_list):
    present_absent = [1,0]
    present_possibility = 0.7
    weights = [present_possibility, 1-present_possibility]
    for student in student_list:
        student_attendance = {}
        for date in date_list:
            student_attendance.update({'{}'.format(date): random.choices(present_absent, weights=weights)[0]})
        student.update({'attendance': student_attendance})


# end of auxiliary functions


#tu poniżej jest funkcja, chciałam zrobić tak żeby tworzyła od razu zmienną o zadanej nazwie
#czy to się tak robi? (zmienna powstaje ale podkreśla na czerwono z dopiskiem "unresoved reference nazwa_zmiennej")
def generate_school_class(name, dates, students):
        globals()[name] = {'name': name, 'dates': dates, 'students': students}

# tu jest wersja która działa, ale trzeba przypisać wynik do nazwy,
# a chciałabym wiedzieć jak wprowadzać nazwę jako argument funkcji
"""
def generate_school_class(dates, students):
    school_class = {'name': name, 'dates': dates, 'students': students}
    return school_class
"""

def class_average(student_name, student_surname, school_class):
    average = None
    for student in school_class['students']:
        if all([student['name'] == student_name, student['surname'] == student_surname]):
            average = sum(student['score'])/len(student['score'])
    return average


def total_average(student_name, student_surname):
    class_averages = []
    for school_class in school_register['classes']:
        for student in school_class['students']:
            if all([student['name'] == student_name, student['surname'] == student_surname]):
                class_averages.append(sum(student['score'])/len(student['score']))
    average = sum(class_averages)/len(class_averages)


school_register = [ ]

#math = {'dates': [], 'students': []}
student = {'name': '', 'surname': '', 'attendance': [], 'scores': []}


if __name__ == "__main__":

    student_list = student_generator(12)

    math_dates = class_date_generator(2023, 2, 13, 7, 5)
    physics_dates = class_date_generator(2023, 2, 14, 7, 6)
    programming_dates = class_date_generator(2023, 2, 16, 7, 7)

    math_students = random.sample(student_list, 5)
    physics_students = random.sample(student_list, 7)
    programming_students = student_list

    generate_attendance(math_dates[:-1], math_students)
    generate_attendance(physics_dates[:-2], physics_students)
    generate_attendance(programming_dates[:-3], programming_students)

    generate_score(3, math_students)
    generate_score(3, physics_students)
    generate_score(3, programming_students)

    #math = {'dates': math_dates, 'students': math_students}
    generate_school_class('math', math_dates, math_students)
    physics = {'dates': physics_dates, 'students': physics_students}
    programming = {'dates': programming_dates, 'students': programming_students}

    school_register = {'class_name': '3b', 'students': student_list, 'classes': [math, physics, programming_students]}

    student1 = '{} {}'.format(physics['students'][0]['name'], physics['students'][0]['surname'])
    class_average1 = class_average(physics['students'][0]['name'], physics['students'][0]['surname'], physics)
    #total_average1 = total_average(physics['students'][0]['name'], physics['students'][0]['surname'])
    print(student1)
    print(class_average1)
    #print(total_average1)
    print(type(school_register['classes'][0]))
    print(physics["students"])