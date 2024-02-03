import itertools
import logging
import gc
import random
import threading


logger1 = logging.getLogger('logger1')
logger1.setLevel(logging.DEBUG)

file1 = logging.FileHandler('history.log')
file1_formatter = logging.Formatter('%(levelname)s:%(message)s')
file1.setFormatter(file1_formatter)
file1.setLevel(logging.DEBUG)
logger1.addHandler(file1)

stream = logging.StreamHandler()
stream_formatter = logging.Formatter('%(levelname)s:%(message)s')
stream.setFormatter(stream_formatter)
logger1.addHandler(stream)


class Account:
    accounts_created = itertools.count(start=1, step=1)

    def __init__(self, bank, owner, money):
        self.bank = bank
        self.owner = owner
        self.money = money
        self.number = self.accounts_created.__next__()

    def __repr__(self):
        return 'number:{} bank:{} owner:{} money:{}'.format( self.number, self.bank, self.owner, self.money)


class Person:

    def __init__(self, name, money_at_hand, accounts):
        self.name = name
        self.accounts = accounts
        self.money_at_hand = money_at_hand
        logger1.debug('person created: [{}]'.format(self))
    def __repr__(self):
        return 'name:{}, money at hand:{}\naccounts:\n{}'.format(self.name,self.money_at_hand, self.accounts)

    def withdraw(self, money, account_number):
        if any(account_number == ac.number for ac in self.accounts):
            selected_account = [ac for ac in self.accounts if ac.number == account_number][0]
            if money <= selected_account.money:
                selected_account.money -= money
                self.money_at_hand += money
                logger1.info('{}: withdrawal successfull.\naccount state: [{}]\n at hand:{}'
                         .format(self.name, selected_account, self.money_at_hand))
            else:
                logger1.error('{} money withdrawal: {} is to much. In account:{}'
                              .format(self.name, money, selected_account.money))
        else:
            logger1.error('{} money withdrawal: wrong account number'.format( self.name) )
            
    def deposit(self, money, account_number):
        if any(account_number == ac.number for ac in self.accounts):
            if money <= self.money_at_hand:
                selected_account = [ac for ac in self.accounts if ac.number == account_number][0]
                selected_account.money += money
                self.money_at_hand -= money
                logger1.info('{}: deposition successfull.\naccount state: [{}]\nstill at hand:{} '.format(self.name, selected_account, self.money_at_hand))
            else:
                logger1.error('{} money depositoin: {} is to much. Only has {} at hand'.format(self.name, money, self.money_at_hand))
        else:
            logger1.error('{} money depositoin: wrong account number'.format(self.name))

    def save_to_file(self):
        with open('clients.txt', 'a') as file:
            file.write('\n{} {}'.format(self.name, self.money_at_hand))


class Bank:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts

    def __repr__(self):
        return 'name:{}\naccounts:{}'.format(self.name, len(self.accounts))

    def create_account(self, owner, money):
       if money <= owner.money_at_hand:
            account = Account(self.name, owner.name, money)
            self.accounts.append(account)
            owner.accounts.append(account)
            owner.money_at_hand -= money
            logger1.info('account created: [{}]'.format(account))
       else:
           logger1.error('{} account creation: to much money selected:{}. {} only has {} at hand'
                         .format(self.name, money, owner.name, owner.money_at_hand))

    def money_transfer(self, principal_ac_number, recipient_ac_number, money):
        recipient_account = []
        if any(principal_ac_number == ac.number for ac in self.accounts):
            principal_account = [ac for ac in self.accounts if ac.number == principal_ac_number][0]
            for account in gc.get_objects():
                if isinstance(account, Account):
                    if recipient_ac_number == account.number:
                        recipient_account = account
            if recipient_account != []:
                if money <= principal_account.money:
                    principal_account.money -= money
                    recipient_account.money += money
                    logger1.info('{} money transfer successful\n transferred:{}\n principal:[{}, {}] -> recipient:[{}, {}]'
                                .format(self.name, money, principal_account.bank, principal_account.owner,
                                         recipient_account.bank, recipient_account.owner))
                else:
                    logger1.error('{} money transfer: to much money selected'.format(self.name,))
            else:
                logger1.error('{} money transfer: wrong recipient account number. account not exist'.format(self.name,))
        else:
            logger1.error('{} money transfer: wrong principal account number. no such account in {}'.format(self.name, self.name))

    @staticmethod
    def advertising_slogan1():
        return 'give us money, we take care of it'

    @staticmethod
    def advertising_slogan2():
        return 'give us money, there\'s no better place'

    @staticmethod
    def pushy(function):
        def wrapper():
            func = function()
            pushy_text = func.upper()+"!!!"
            return pushy_text
        return wrapper

def generate_clients_data(people_number):
    names = ['Ann', 'Mark', 'Tom', 'Jane', 'Tina', 'Julia', 'Victoria']
    money = ['100', '200', '300', '345', '500', '50']
    people_list = []
    i = 1
    while i <= people_number:
        next_person = random.choice(names) + " " + random.choice(money)
        if all(next_person != p for p in people_list):
            people_list.append(next_person)
            i += 1
        else:
            continue
    logger1.debug('clients data generated: {}'.format(people_list))
    return people_list

def clients_data_from_file(file_name):
    with open(file_name, 'r') as file:
        clients = file.readlines()
    for client in clients:
        clients[clients.index(client)] = client.replace('\n','')
    logger1.debug('{} clients data uploaded:{}'.format(len(clients), clients))
    return clients

def people_from_data(clients):
    for client in clients:
        client = client.split()
        client[0] = Person(client[0], int(client[1]), [])


if __name__ == "__main__":

    #tial run:
    clients_generated = generate_clients_data(3)
    clients_uploaded = clients_data_from_file('clients.txt')

    t1 = threading.Thread(target=people_from_data, args=(clients_generated,))
    t2 = threading.Thread(target=people_from_data, args=(clients_uploaded,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


    b1 = Bank('b1', [])
    b2 = Bank('b2', [])

    Mark = Person('Mark', 300, [])
    Ann = Person('Ann',200, [])
    Tom = Person('Tom', 250, [])

    Ann.save_to_file()
    Mark.save_to_file()
    Tom.save_to_file()

    b1.create_account(Mark,23)
    b1.create_account(Ann, 301)
    b1.create_account(Ann, 12)

    Mark.deposit(25,3)
    Mark.deposit(400, 1)
    Mark.deposit(25,1)

    Ann.withdraw(25,4)
    Ann.withdraw(300,2)
    Ann.withdraw(5,2)

    b2.create_account(Tom,150)
    b2.money_transfer(15,2,20)
    b2.money_transfer(3, 20, 20)
    b2.money_transfer(3, 2, 300)
    b2.money_transfer(3, 2, 20)

    logger1.info(b2.advertising_slogan1())
    pushy_ad = b2.pushy(b2.advertising_slogan2)
    logger1.info(pushy_ad())
