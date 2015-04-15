__author__ = 'Jim'
import unittest
'''& and | used are bitwise operator while 'not' is logical not not bitwise not'''
def duplicates_string(str):
    flag = 0
    result = ''
    for i in str:
        b = 1<<ord(i)
        if not(flag&b):
            result += i
            flag |=b
    return result

class DuplicateTestcase(unittest.TestCase):
    TEST_DATA = [
        "Jithuuu",'Jithu',
        "Jithinnnn",'Jithn',
        "Jimuminm","Jimun"
    ]

    def duplicatestringtest(self):
        for str,expected in self.TEST_DATA:
            result = duplicates_string(str)
            self.assertEquals(result,expected)

if __name__=="__main__":
    unittest.main()



