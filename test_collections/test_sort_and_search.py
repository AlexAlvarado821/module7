import unittest
from fun_with_collections import sort_and_search_list

class MyTestCase(unittest.TestCase):
    def test_not_in_list(self):
        self.assertEqual(sort_and_search_list.search_list("Random"), -1)

    def test_in_list(self):
        self.assertEqual(sort_and_search_list.search_list("Bailey"), 1 )



if __name__ == '__main__':
    unittest.main()
