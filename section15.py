# Testing
import unittest
import section14

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = section14.do_stuff(test_param)
        self.assertEqual(result, 15)
        
    def test_do_stuff2(self):
        test_param = 'cindrella'
        result = section14.do_stuff(test_param)
        self.assertTrue(isinstance(result, TypeError)) # methods in unit_testing
        #self.assertIsInstance(result, TypeError)
        
unittest.main()