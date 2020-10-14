import unittest
from unittest.mock import patch
from fun_with_collections import basic_list

class MyTestCase(unittest.TestCase):
    # the patch will return a value for get input even though there is nothing in the function 
    @patch('fun_with_collections.basic_list.get_input', return_value='5')
    def test_something(self, input):
        self.assertEqual(basic_list.make_list(), [5, 5, 5])


if __name__ == '__main__':
    unittest.main()
