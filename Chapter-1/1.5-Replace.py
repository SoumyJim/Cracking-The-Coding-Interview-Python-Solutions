import unittest
__author__ = 'Jim'

def replace_string(str):
    return str.replace("","%20")

class ReverseString(unittest.TestCase):
    TEST_DATA = [

        "Jith u","Jith%20u",
        "J im","J%20im",
        "ki m","ki%20m"
    ]

    def reversedStringTest(self):
        for str,expected_result in self.TEST_DATA:
            result = replace_string(str)
            self.assertEquals(result,expected_result)


if __name__ == "__main__":
    unittest.main()
