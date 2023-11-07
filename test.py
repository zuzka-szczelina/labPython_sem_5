import unittest
from models.client import Client


class TestTask(unittest.TestCase):


    def test_accept_payment(self):
        c1 = Client(20, 30,'Ann', 'some address', 300)
        c1.accept_payment(5)
        self.assertEqual(c1.money,305)



if __name__ == '__main__':
    unittest.main()
