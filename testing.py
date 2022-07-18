import unittest
import HtmlTestRunner

from bubble import bubble_sort

class TestInt(unittest.TestCase):
    def test_all_pos_small(self):
        test = [3, 1, 7, 8, 2, 4]
        self.assertEqual(bubble_sort(test), sorted(test))
    
    def test_all_pos_medium(self):
        test = [2323, 123, 923, 823, 2, 4]
        self.assertEqual(bubble_sort(test), sorted(test))
    
    def test_all_post_large(self):
        test = [23920390293, 10232103, 102391029301293, 23923901920392031, 85748751929813822323]
        self.assertEqual(bubble_sort(test), sorted(test))
    

class TestStr(unittest.TestCase):
    def test_letters(self):
        test = ['a', 'b', 'c', 'd', 'e']
        self.assertEqual(bubble_sort(test), sorted(test))
    
    def test_words(self):
        test = ['hello', 'world', 'this', 'is', 'a', 'test']
        self.assertEqual(bubble_sort(test), sorted(test))

    def test_chars(self):
        test = ['a', '1', 'b', '2', 'c', '3']
        self.assertEqual(bubble_sort(test), sorted(test))


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))