import bigbus
import unittest
import datetime
from datetime import timedelta  

today = datetime.datetime.now()

class BigBusTest(unittest.TestCase):

    def test_yesterday(self):
        yday = today - datetime.timedelta(days=1)
        self.assertNotIn(yday, bigbus.dates)

    # def test_1(self):
    #     machine = CoinMachine()
    #     coins = machine.dispense(1)
    #     self.assertEqual([0,0,0,1], coins)

    # def test_4(self):
    #     machine = CoinMachine()
    #     coins = machine.dispense(4)
    #     self.assertEqual([0,0,0,4], coins)

    # def test_5(self):
    #     machine = CoinMachine()
    #     coins = machine.dispense(5)
    #     self.assertEqual([0,0,1,0], coins)

    # def test_6(self):
    #     machine = CoinMachine()
    #     coins = machine.dispense(6)
    #     self.assertEqual([0,0,1,1], coins)

    # def test_10(self):
    #     machine = CoinMachine()
    #     coins = machine.dispense(10)
    #     self.assertEqual([0,1,0,0], coins)

    # def test_15(self):
    #     machine = CoinMachine()
    #     coins = machine.dispense(15)
    #     self.assertEqual([0,1,1,0], coins)

    # def test_25(self):
    #     machine = CoinMachine()
    #     coins = machine.dispense(25)
    #     self.assertEqual([1,0,0,0], coins)

    # def test_50(self):
    #     machine = CoinMachine()
    #     coins = machine.dispense(50)
    #     self.assertEqual([2,0,0,0], coins)
    # #
    # def test_99(self):
    #     machine = CoinMachine()
    #     coins = machine.dispense(99)
    #     self.assertEqual([3,2,0,4], coins)
    #
    # def test_not_enough_quarters(self):
    #     machine = CoinMachine([0, 10, 10, 10])
    #     coins = machine.dispense(99)
    #     self.assertEqual([0, 9, 1, 4], coins)
    #
    # def test_not_enough_money(self):
    #     machine = CoinMachine([0, 0, 10, 10])
    #     coins = machine.dispense(99)
    #     self.assertEqual(None, coins)
    #
    # def test_not_enough_quarters_then_out_of_money(self):
    #     machine = CoinMachine([0, 10, 10, 10])
    #     coins = machine.dispense(99)
    #     self.assertEqual([0, 9, 1, 4], coins)
    #     coins = machine.dispense(99)
    #     self.assertEqual(None, coins)

unittest.main()

