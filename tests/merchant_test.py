import unittest
from models.merchant import *

class TestMerchant(unittest.TestCase):
    
    def setUp(self):
        self.merchant1 = Merchant('Tesco')
        
    def test_default_activated_merchant(self):
        self.assertEqual(True, self.merchant1.activated)
    
    def test_flip_activated_merchant(self):
        self.merchant1.flip_activated()
        self.assertEqual(False, self.merchant1.activated)
        self.merchant1.flip_activated()
        self.assertEqual(True, self.merchant1.activated)
        