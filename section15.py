# Testing
import unittest
import section14

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')
    def test_do_stuff(self):
        test_param = 10
        result = section14.do_stuff(test_param)
        self.assertEqual(result, 15)
        
    def test_do_stuff2(self):
        test_param = 'cindrella'
        result = section14.do_stuff(test_param)
        self.assertTrue(isinstance(result, TypeError)) # methods in unit_testing
        # self.assertIsInstance(result, TypeError)
        
    def test_do_stuff3(self):
        test_param = None
        result = section14.do_stuff(test_param)
        self.assertIsInstance(result, TypeError)
        
    def tearDown(self):
        print('cleaning Up')

if __name__ == '__main__':
    unittest.main()