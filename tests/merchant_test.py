import unittest
from models.merchant import *

class TestAccount(unittest.TestCase):
    
    def setUp(self):
        self.merchant1 = Merchant('Tesco')
        