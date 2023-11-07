from typing import List, Callable

from models.client import Client


class Bank:
    clients: List[Client]
    __external_transfer_callable: Callable[[int, int, float], bool]

    def __init__(self, external_transfer_callable: Callable[[int, int, float], bool]):
        self.clients = []
        self.__external_transfer_callable = external_transfer_callable

    def create_new_client(self, name: str, address: str, money: float = 0):
        self.clients.append(
            Client(
                name=name,
                address=address,
                money=money,
                external_transfer=self.__make_external_payment,
                internal_transfer=self.make_internal_payment
            )
        )

    def make_internal_payment(self, to_index: int, amount_of_money: float):
        if 0 <= to_index < len(self.clients):
            self.clients[to_index].accept_payment(amount_of_money)
            return True
        return False

    def __make_external_payment(self, bank_index: int, to_index: int, amount_of_money: float):
        return self.__external_transfer_callable(bank_index, to_index, amount_of_money)
