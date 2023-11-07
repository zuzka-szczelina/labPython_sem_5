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
import logging

from models.environment import Environment

if __name__ == "__main__":
    environment = Environment()

    while True:
        print(
            "What would you want to do?\n"
            "1. Create new bank\n"
            "2. Pick an existing bank"
        )
        value = input()

        if value == "1":
            environment.create_bank()
            print("created")

        if value == "2":
            index = 0
            for bank in environment.banks:
                print("{}. ".format(index))
                index += 1

            print("Pick a bank:")
            bank_index = input()

            if 0 <= int(bank_index) < len(environment.banks):
                index = 0
                for client in environment.banks[index].clients:
                    print("{}. ".format(index))
                    index += 1

                print("Pick a client:")
                client_index = input()

