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

class Student:
    def __init__(self,name, classes, attendance, scores):
        self.name = name
        self.classes = classes
        self.attendance = attendance
        self.scores = scores

class Class:
    def __init__(self, name, students, attendance, scores):
        self.name = name
        self.students = students
        self.attendance = attendance
        self.scores = scores

    def average_score(self, student):
        student_index = self.students.index(student)
        average = (sum(self.scores[student_index])/len(self.scores[student_index]) for s in self.students if s == self.student)
        return average




class GradeBook:
    def __init__(self, students, classes):
        self.students = students
        self.classes = classes

    def average_score(self, student):
        pass

"""
A = 
GB = GradeBook(["A", "B", "C"])
C1 = Class("C1", ["A","B"], )
"""