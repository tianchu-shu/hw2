import bigbus
import backend
import unittest
import datetime
from datetime import timedelta 


today = datetime.datetime.now()

class BigBusTest(unittest.TestCase):

    def test_yesterday(self):
        yday = today - datetime.timedelta(days=1)
        yday = yday.strftime('%m/%d/%Y')
        self.assertNotIn(yday, bigbus.dates)


    def test_11day(self):
        nday = today + datetime.timedelta(days=11)
        nday = nday.strftime('%m/%d/%Y')
        self.assertNotIn(nday, bigbus.dates)


    def test_5day(self):
        day = today + datetime.timedelta(days=5)
        day = day.strftime('%m/%d/%Y')
        self.assertIn(day, bigbus.dates)


    def test_discount(self):
        day = today + datetime.timedelta(days=5)
        day = day.strftime('%m/%d/%Y')
        answers = {'amount': '4', 'date': day, 'route': 'Green'}
        total = bigbus.checkout(answers)
        tprice = bigbus.price[day]
        amt = 4 * tprice * 0.9
        self.assertEqual(amt, total)


    def test_soldout(self):
        day = today + datetime.timedelta(days=5)
        day = day.strftime('%m/%d/%Y')
        answers = {'amount': '4', 'date': day, 'route': 'Green'}
        tally = backend.tally
        tally[day]['Green'] = 0
        with self.assertRaises(ValueError):
            bigbus.ticketvalidate(answers, tally, backend.report)


    def test_unvalid_ticket(self):    
        with self.assertRaises(KeyError):
            bigbus.confirm_refund('', backend.stock, backend.tally)

            
    def test_refund(self):
        self.assertEqual(177, backend.tally[backend.dates[6]]['Blue'])
        bigbus.confirm_refund('a1cde9b2-f132-4e0b-b5cb-6668a0c54328', backend.stock, backend.tally)
        self.assertEqual(178, backend.tally[backend.dates[6]]['Blue'])


    def test_double_refund(self):
        bigbus.confirm_refund('c56c67ce-f8dd-4da9-a59c-fb2a02f74c1a', backend.stock, backend.tally)
        with self.assertRaises(KeyError):
            bigbus.confirm_refund('c56c67ce-f8dd-4da9-a59c-fb2a02f74c1a', backend.stock, backend.tally)
        
 


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

