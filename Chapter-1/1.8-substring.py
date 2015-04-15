__author__ = 'Jim'
import unittest
def find_substring(str1,str2):
    length = len(str1)
    if length == 0 or length != len(str2):
        return False
    return (str1+str2).find(str2) != -1

class MyTestCases(unittest.TestCase):
    def test_mycase(self):
        self.demo = find_substring
        self.assertEqual(self.demo("abab", "ab"), False)
        self.assertEqual(self.demo("ab", "abab"), False)
        self.assertEqual(self.demo("abab", "abab"), True)
        self.assertEqual(self.demo("abab", "baba"), True)
        self.assertEqual(self.demo("erbottlewat", "waterbottle"), True)
        self.assertEqual(self.demo("waterbottle", "erbottlewat"), True)
if __name__ == '__main__':
    unittest.main()