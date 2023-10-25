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

#wpłacanie i wypłacanie pieniędzy
#pieniądze "u osoby" i w poszczególnych bankach - zeby częśc zostawała jako dostępne a częśc szłą do banku
#info że imię/nazwa baku się powtórzyła

class Bank:
  def __init__(self, name, person_list ):
    self.name = name
    self.person_list = person_list

class Person:
  def __init__(self, name, money_at_hand, money_in_banks ):
    self.name = name
    self.money_at_hand = money_at_hand
    self.money_in_banks = money_in_banks

  def money_deposition(self, money):
    pass
  def money_deposition(self, money):
    pass

if __name__ == "__main__":

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
      #dodać mechanizm żeby był błąd jeśli input nie liczba int
      money = int(input())
      person_name = Person(person_name, money, 0)
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
  while answer != "no":
    if answer == "yes":
      print("type person's name, you can choose from: {}".format(list(i.name for i in person_list)))
      person_input = input()
      person_to_add = [obj for obj in person_list if obj.name == person_input]
      if person_to_add == []:
        print("there's no such person, try one more time")
        continue
      else:
        person_to_add = person_to_add[0]
      print("now choose the bank, you can choose from: {}".format(list(i.name for i in bank_list)))
      bank_input = input()
      bank_chosen = [obj for obj in bank_list if obj.name == bank_input ]
      if bank_chosen == []:
        print("there's no such bank, try one more time")
        continue
      else:
        bank_chosen = bank_chosen[0]

      print("how much money you want to deposit? {} sill has {} to deposit.".format(person_to_add.name, person_to_add.money_at_hand))
      money_to_deposit = int(input())
      if money_to_deposit <= person_to_add.money_at_hand :
        person_to_add.money_at_hand -= money_to_deposit
        person_to_add.money_in_banks += money_to_deposit
        #trzeba słownikiem nie listą żeby się dało znaleźć łatwiej info o osobie po imieniu (chyba)
        bank_chosen.person_list.append([person_to_add.name, money_to_deposit])
        print("success! {}'s {} account: {} money".format(person_to_add.name, bank_chosen.name, money_to_deposit))
      else:
        print("This person doesn't have that much to deposit. Try one more time.")
        continue
      print("do you want to add another person to a bank? type: yes or no")
      answer = input()
      continue
    elif any(answer != i for i in ["yes", "no"]):
      print("Your answer is neither \"yes\" nor \"no\". Please type it one more time.")
      answer = input()
      continue


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