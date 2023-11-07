from typing import List

from models.bank import Bank


class Environment:
    banks: List[Bank]

    def __init__(self):
        self.banks = []

    def create_bank(self):
        self.banks.append(
            Bank(
                external_transfer_callable=self.__external_transfer_callable
            )
        )

    def __external_transfer_callable(self, bank_index: int, to_index: int, amount_of_money: float):
        if 0 <= bank_index < len(self.banks):
            return self.banks[bank_index].make_internal_payment(to_index, amount_of_money)
        return False
