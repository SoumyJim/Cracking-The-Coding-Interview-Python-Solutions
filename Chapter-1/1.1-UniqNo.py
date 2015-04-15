__author__ = 'Jim'

import unittest

def no_duplicates(str):
    #Change request after 2 months to handle numeric inputs differently!
    if type(str)==int:
        return False

    for f in str:
        if str.count(f) > 1:
            return False
    return True

#print(no_duplicates("Mee"))

#Tests
class NoDuplicatesTest(unittest.TestCase):

    # Two-element tuples: input string and expected result

    TEST_DATA = [
        ('Me', True),
        ('Mee', False),
        ('ab', True),
        ('ab ', True),
        (22,False),
        (2,False),
        ('', True),
       # (' ', False),
        #('  ', False),
        ('qwerty', True),
        ('qwerte', False)]

    def test_no_duplicates_both_versions(self):
        for str_, expected_result in self.TEST_DATA:
            result = no_duplicates(str_)
            self.assertEqual(result, expected_result)

            # Test the version without additional data structures too
            #result2 = no_duplicates_no_structures(str_)
            #self.assertEqual(result2, expected_result)

if __name__ == "__main__":
    unittest.main()