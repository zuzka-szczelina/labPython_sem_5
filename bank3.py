import itertools
import logging
import gc


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

# - mogę dodać historię konta
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
        return 'name:{}\nmoney at hand:{}\naccounts:\n{}'.format(self.name,self.money_at_hand, self.accounts)

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

    def money_transfer(self,principal_ac_number, recipient_ac_number, money):
        if any(principal_ac_number == ac.number for ac in self.accounts):
            principal_account = [ac for ac in self.accounts if ac.number == principal_ac_number][0]
            for account in gc.get_objects():
                if isinstance(account, Account):
                    if recipient_ac_number == account.number:
                        recipient_account = account
                        if money <= principal_account.money:
                            principal_account.money -= money
                            recipient_account.money += money
                            logger1.info('money transfer successful\n transferred:{}\n principal:{}{}->recipient:{}{}'
                                         .format(money, principal_account.bank, principal_account.owner,
                                                 recipient_account.bank, recipient_account.owner))
                        else:
                            logger1.error('{} money transfer: to much money selected'.format(self.name,))


                    else:
                        logger1.error('{} money transfer: wrong recipient account number'.format(self.name,))
        else:
            logger1.error('{} money transfer: wrong principal account number'.format(self.name,))


if __name__ == "__main__":

#trial run:
  b1 = Bank('b1', [])
  Mark = Person('Mark', 300, [])
  Ann = Person('Ann',200, [])

  b1.create_account(Mark,23)
  b1.create_account(Ann, 301)
  b1.create_account(Ann, 12)

  Mark.deposit(25,3)
  Mark.deposit(400, 1)
  Mark.deposit(25,1)

  Ann.withdraw(25,4)
  Ann.withdraw(300,2)
  Ann.withdraw(5,2)
