import unittest
from models.transaction import *
from models.merchant import *
from models.category import *

class TestAccount(unittest.TestCase):
    
    def setUp(self):
        
        self.merchant1 = Merchant('Tesco')
        self.category1 = Category('Groceries')
        
        self.transaction1 = Transaction('2022-04-27', merchant1, 999, category1)
        
        
        