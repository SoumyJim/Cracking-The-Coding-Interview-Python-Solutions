__author__ = 'Jim'
import unittest

def reverse_string(str):
    return str[::-1]


class ReverseString(unittest.TestCase):
    TEST_DATA = [

        "Jithu","uhtiJ",
        "Jim","miJ",
        "ki m","m ik"
    ]

    def reversedStringTest(self):
        for str,expected_result in self.TEST_DATA:
            result = reverse_string(str)
            self.assertEquals(result,expected_result)


if __name__ == "__main__":
    unittest.main()