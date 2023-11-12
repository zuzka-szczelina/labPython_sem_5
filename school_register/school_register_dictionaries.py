import random
import datetime
import json
from copy import copy
import example_register_generation


def class_average(school_class, student_name, student_surname):
    average = None
    for student in school_class['students']:
        if all([student['name'] == student_name, student['surname'] == student_surname]):
            average = sum(student['score'])/len(student['score'])
    return average


def total_average(register_name, student_name, student_surname):
    class_averages = []
    for school_class in register_name['classes'].values():
        for student in school_class['students']:
            if all([student['name'] == student_name, student['surname'] == student_surname]):
                class_averages.append(sum(student['score'])/len(student['score']))
    average = sum(class_averages)/len(class_averages)
    return average


if __name__ == "__main__":

    with open('register.json') as f:
       register = json.load(f)
    print("whole register:\n{}".format(json.dumps(register, indent=2)))

    school_class = register['classes']['physics']
    student_name = school_class['students'][0]['name']
    student_surname = school_class['students'][0]['surname']

    class_average1 = class_average(school_class,student_name,student_surname)
    print("{} {} average in {} is {}"
          .format(student_name, student_surname, school_class['name'], class_average1))

    total_average1 = total_average(register, student_name, student_surname)
    print("{} {} total average is {}"
          .format(student_name, student_surname, total_average1))