import logging
from typing import Callable


class Client:
    __internal_transfer_callable: Callable[[int, float], bool]
    __external_transfer_callable: Callable[[int, int, float], bool]
    name: str
    address: str
    money: float

    def __init__(
            self,
            internal_transfer: Callable[[int, float], bool],
            external_transfer: Callable[[int, int, float], bool],
            name: str,
            address: str,
            money: float = 0.0
    ):
        self.__internal_transfer_callable = internal_transfer
        self.__external_transfer_callable = external_transfer
        self.name = name
        self.address = address
        self.money = money

    def make_internal_payment(self, amount_of_money: float, to_index: int):
        if self.money >= amount_of_money:
            successful = self.__internal_transfer_callable(to_index, amount_of_money)
            if successful:
                self.money -= amount_of_money
                logging.info("Transfer successful!")
            else:
                logging.error("No such client!")
        else:
            logging.error("You don't have enough money!")

    def make_external_payment(self, amount_of_money: float, to_index: int, bank_index: int):
        if self.money >= amount_of_money:
            successful = self.__external_transfer_callable(bank_index, to_index, amount_of_money)
            if successful:
                self.money -= amount_of_money
                logging.info("Transfer successful!")
            else:
                logging.error("No such client or bank!")
        else:
            logging.error("You don't have enough money!")

    def make_withdrawal(self, amount_of_money):
        if self.money >= amount_of_money:
            self.money -= amount_of_money
            logging.info("Transfer successful!")
        else:
            logging.error("You don't have enough money!")

    def accept_payment(self, amount_of_money):
        self.money += amount_of_money

