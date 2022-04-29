import unittest
from models.category import *

class TestCategory(unittest.TestCase):
    
    def setUp(self):
        self.category1 = Category('Groceries')
        
    def test_default_activated_category(self):
        self.assertEqual(True, self.category1.activated)
    
    def test_flip_activated_category(self):
        self.category1.flip_activated()
        self.assertEqual(False, self.category1.activated)
        self.category1.flip_activated()
        self.assertEqual(True, self.category1.activated)
        
        