import unittest
from fun_with_collections import sort_and_search_list

class MyTestCase(unittest.TestCase):
    def test_not_in_list(self):
        self.assertEqual(sort_and_search_list.search_list("Random"), "The target is not located in the list")

    def test_in_list(self):
        self.assertEqual(sort_and_search_list.search_list("Bailey"), "The target is located in the list" )



if __name__ == '__main__':
    unittest.main()
