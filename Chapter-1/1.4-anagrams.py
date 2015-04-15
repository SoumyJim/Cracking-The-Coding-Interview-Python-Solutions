__author__ = 'Jim'
import unittest

def anagram_string(str1,str2):
    return "".join(sorted(str1))== "".join(sorted(str2))

class AnagramTest(unittest.TestCase):
    def test_case(self):
        self.assertEqual(anagram_string("Jithu","Jithu"),True)
        self.assertEqual(anagram_string("Jim","miJ"),True)

if __name__ == "__main__":
    unittest.main()

