from datetime import date
import unittest
from models.transaction import *
from models.merchant import *
from models.category import *

class TestTransaction(unittest.TestCase):
    
    def setUp(self):
        
        self.merchant1 = Merchant('Tesco')
        self.category1 = Category('Groceries')
        self.transaction1 = Transaction('2022-04-27', self.merchant1, 999, self.category1)
        self.transaction2 = Transaction('2022-10-27', self.merchant1, 999, self.category1)
        self.transaction3 = Transaction('2022-04-01', self.merchant1, 999, self.category1)
        
        self.date_string = '2022-04-27'

        
        
    def test_currency_format (self):
        self.assertEqual('£9.99',self.transaction1.currency_format())
        
    def test_date_format(self):
        self.assertEqual('27-04-2022',self.transaction1.date_format())
        self.assertEqual('27-10-2022',self.transaction2.date_format())
        self.assertEqual('01-04-2022',self.transaction3.date_format())
        
    def test_string_to_date__string (self):
        date_string_check = Transaction.string_to_date(self.date_string)
        self.assertIsInstance(date_string_check, date)
  

    def test_string_to_date__date (self):
        date_string_check = Transaction.string_to_date(self.date_string)
        date_check = Transaction.string_to_date(date_string_check)
        self.assertIsInstance(date_check, date)