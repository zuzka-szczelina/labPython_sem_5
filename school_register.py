# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.
"""

class Student:
    def __init__(self,name, classes, attendance, scores):
        self.name = name
        self.classes = classes
        self.attendance = attendance
        self.scores = scores


"""

import random
import datetime

class SchoolClass:
    def __init__(self, name, students, scores, attendance):
        self.name = name
        self.students = students
        self.attendance = attendance
        self.scores = scores

    def __repr__(self):
        return "{}\nnumber of students: {}\n lessons taken {}".format(self.name, len(self.students), len(self.attendance))

    def average_score(self, student):
        student_index = self.students.index(student)
        student_score = self.scores[student_index]
        average = sum(student_score)/len(student_score)
        return average



#mogę dodać info o charakterystykach: ile już było zajęć ile jeszcze ile wgl ma być
class GradeBook:
    def __init__(self, students, classes):
        self.students = students
        self.classes = classes


    def average_score(self, student):
        pass


def student_generator(number_of_students):
    names = ['Ann', 'Mark', 'Tom', 'Jane', 'Tina']
    surnames = ['Smith', 'Brown', 'Johnson', 'Walker', 'Gray']
    student_list = []
    for i in range(number_of_students):
        student_list.append(random.choice(names) + " " + random.choice(surnames))
    return student_list

def score_generator(number_of_grades, number_of_students):
    grades = [2,3,4,5]
    score_list = []
    for i in range(number_of_students):
        one_student_score = random.choices(grades, k=number_of_grades)
        score_list.append(one_student_score)
    return score_list

def class_date_generator( start_year, start_month,start_day , step, number_of_lessons):
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
def attendance_generator(date_list, number_of_students):
    present_absent = [1,0]
    present_possibility = 0.7
    weights = [present_possibility, 1-present_possibility]
    attendance = []
    for date in date_list:
        students_presence = random.choices(present_absent, weights=weights, k=number_of_students)
        date_attendance = {"{}".format(date): students_presence}
        attendance.append(date_attendance)
    return attendance


if __name__ == "__main__":
#dodać żeby się dało dopisywać studentów, attendance każdego po kolei (pod konkretną datą), score
#test class:

    #generating some random school class data
    student_list = student_generator(4)
    math = SchoolClass("math",random.sample(student_list, 3),[],[] )
    dates = class_date_generator(2023,2,13,7,5)
    at = attendance_generator(dates, len(math.students))
    score = score_generator(3,len(math.students))
    print(math)