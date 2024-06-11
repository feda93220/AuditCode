import unittest
from src.main import add

class TestMain(unittest.TestCase):
    def test_add(self):
         # Test avec les valeurs 2 et 4
        self.assertEqual(add(2, 4), 6)
        
        # Test avec les valeurs -1 et 3
        self.assertEqual(add(-1, 3), 2)
        
        # Test avec les valeurs -1 et -2
        self.assertEqual(add(-1, -2), -3)
        
        self.assertNotEqual(add(2, 50), 30)

if __name__== '__main__':
    unittest.main()