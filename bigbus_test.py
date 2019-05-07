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
        day = today + datetime.timedelta(days=4)
        day = day.strftime('%m/%d/%Y')
        answers = {'amount': '3', 'date': day, 'route': 'Blue'}
        tally = backend.tally
        tally[day]['Blue'] = 0
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
        
        
    def test_past_refund(self):    
        with self.assertRaises(KeyError):
            bigbus.confirm_refund('71a16ad0-1426-4dfa-943e-76b76cab4202', backend.stock, backend.tally)
     
 
    def test_buy(self):
        day = today + datetime.timedelta(days=2)
        day = day.strftime('%m/%d/%Y')
        answers = {'amount': '2', 'date': day, 'route': 'Red'}
        l = len(backend.stock)
        newstock = bigbus.confirm(answers, backend.tally, backend.stock, backend.report)
        self.assertEqual(len(newstock), l+2)



unittest.main()

