import unittest

from fun_with_collections import sort_and_search_array

class MyTestCase(unittest.TestCase):
    def test_valid_number(self):
        self.assertEqual(sort_and_search_array.search_array(3), '2')

    def test_invalid_number(self):
        self.assertEqual(sort_and_search_array.search_array(20), '-1')


if __name__ == '__main__':
    unittest.main()
