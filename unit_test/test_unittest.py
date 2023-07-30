import unittest
from unittest import result
import Unit_Test

class Testunit(unittest.TestCase):
    def test_add(self):
        result=Unit_Test.add(10,5)
        self.assertEqual(result,15)

if __name__=='__main__':
    unittest.main()
