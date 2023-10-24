#
#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can think of any other features, you can add them.
#This code shoud be runnable with 'python task.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
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


class Bank:
  def __init__(self, name, person_list ):
    self.name = name
    self.person_list = person_list

class Person:
  def __init__(self, name, money ):
    self.name = name
    self.money = money

if __name__ == "__main__":
  p1 = Person("john", 34)
  print(type(p1))

  print("do you want to create a bank? type: yes or no")
  answer = input()
  bank_list = []

  while answer != "no":
    if answer == "yes":
      print("chose the name of a bank")
      bank_name = input()
      bank_name = Bank(bank_name, [])
      bank_list.append(bank_name)
      print("do you want to create another one? type: yes or no")
      answer = input()
      continue
    # elif any([answer != "yes", answer != "no"]): #tak też git dla tylko 2 opcji
    elif any(answer != i for i in ["yes", "no"]):
      print("Your answer is neither \"yes\" nor \"no\". Please type it one more time.")
      answer = input()
      continue

  """
  #stara wersja - reaguje tak samo na "dowolny tekst" jak na "no"
  while answer == "yes":
    print("chose the name of a bank")
    bank_name = input()
    bank_name = Bank(bank_name, [])
    bank_list.append(bank_name)
    print("do you want to create another one? type: yes or no")
    answer = input()
 """

  print("do you want to create a person? type: yes or no")
  answer = input()
  person_list = []
  while answer != "no":
    if answer == "yes":
      print(f"chose the name of a person")
      person_name = input()
      print(f"amount of money?")
      money = input()
      person_name = Person(person_name, money)
      person_list.append(person_name)
      print("do you want to create another one? type: yes or no")
      answer = input()
      continue
    elif any(answer != i for i in ["yes", "no"]):
      print("Your answer is neither \"yes\" nor \"no\". Please type it one more time.")
      answer = input()
      continue

  print("do you want add any person to a bank? type: yes or no")
  answer = input()
  while answer == "yes":
    print("type person's name, you can choose from: {}".format(list(i.name for i in person_list)))
    person_input = input()
    person_to_add = [obj if obj.name == person_input else print("there's no such person") for obj in person_list][0]
    print("now choose the bank, you can choose from: {}".format(list(i.name for i in bank_list)))
    bank_input = input()
    bank_chosen = [obj if obj.name == bank_input else print("there's no such bank") for obj in bank_list][0]
    bank_chosen.person_list.append(person_to_add)
    print("do you want to add another one? type: yes or no")
    answer = input()



"""
#taki fragment którego nie użyłam ostatecznie ale fajny
import gc

  bank_list = []
  for obj in gc.get_objects():
    if isinstance(obj, Bank):
      bank_list.append(obj.name)

  person_list = []
  for obj in gc.get_objects():
    if isinstance(obj, Person):
      person_list.append(obj.name)
"""