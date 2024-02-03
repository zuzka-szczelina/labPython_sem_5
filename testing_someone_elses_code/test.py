import unittest
from models.client import Client
from models.environment import Environment
from models.bank import Bank


# 10 tests
class TestTask(unittest.TestCase):

    def setUp(self):
        self.e1 = Environment()
        self.e1.create_bank()
        self.e1.create_bank()
        self.b1 = self.e1.banks[0]
        self.b2 = self.e1.banks[1]
        self.b1.create_new_client('Ann', 'Ann\'s address', 300)
        self.b1.create_new_client('Mark', 'MArk\'s address', 250)
        self.c11 = self.b1.clients[0]
        self.c12 = self.b1.clients[1]
        self.b2.create_new_client('Tom', 'Tom\'s address', 350)
        self.c21 = self.b2.clients[0]

    # testing Client
    def test_Client___init__(self):
        self.assertEqual(self.c11.money, 300)
        self.assertEqual(self.c11.address, 'Ann\'s address')
        self.assertEqual(self.c11.name, 'Ann')

    def test_client_make_internal_payment__internal_transfer_callable(self):
        def argument_test(a, b):
            self.assertEqual(a, 1)
            self.assertEqual(b, 20)
            return True

        self.c21 = Client(argument_test, lambda a, b, c: True, 'Ann', 'some address', 300)
        self.c21.make_internal_payment(20, 1)

    def test_client_make_internal_payment_successful(self):
        self.c11.make_internal_payment(30, 1)
        self.assertEqual(self.c11.money, 270)
        self.assertEqual(self.c12.money, 280)

    def test_client_make_internal_payment_index_error(self):
        self.c11.make_internal_payment(30, 3)
        self.assertEqual(self.c11.money, 300)
        self.assertEqual(self.c12.money, 250)

    def test_client_make_internal_payment_money_error(self):
        self.c11.make_internal_payment(3000, 1)
        self.assertEqual(self.c11.money, 300)
        self.assertEqual(self.c12.money, 250)

    def test_client_make_external_payment__external_transfer_callable(self):
        def argument_test(a, b, c):
            self.assertEqual(a, 1)
            self.assertEqual(b, 0)
            self.assertEqual(c, 20)

        self.b3 = Bank(argument_test)
        self.b3.create_new_client('Ann', 'some address', 300)
        self.c31 = self.b3.clients[0]
        self.c31.make_external_payment(20, 0, 1)

    def test_client_make_external_payment_successful(self):
        self.c11.make_external_payment(30, 0, 1)
        self.assertEqual(self.c11.money, 270)
        self.assertEqual(self.c21.money, 380)

    def test_client_make_external_payment_index_error(self):
        self.c11.make_external_payment(30, 0, 3)
        self.assertEqual(self.c11.money, 300)
        self.assertEqual(self.c21.money, 350)

    def test_client_make_external_payment_money_error(self):
        self.c11.make_external_payment(3000, 0, 1)
        self.assertEqual(self.c11.money, 300)
        self.assertEqual(self.c21.money, 350)

    def test_accept_payment(self):
        self.c11.accept_payment(5)
        self.assertEqual(self.c11.money, 305)

    def test_make_withdrawal(self):
        self.c11.make_withdrawal(30)
        self.assertEqual(self.c11.money, 270)
        self.c11.make_withdrawal(280)
        self.assertEqual(self.c11.money, 270)


if __name__ == '__main__':
    unittest.main()
