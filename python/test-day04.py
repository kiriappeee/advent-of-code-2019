import unittest
from . import day04

class TestDay4(unittest.TestCase):
    def test_password_is_validated_correctly(self):
        self.assertTrue(day04.is_password_valid('111111'))
        self.assertTrue(day04.is_password_valid('123455'))
        self.assertFalse(day04.is_password_valid('111230'))

    def test_password_is_validated_correctly_with_new_criteria(self):
        self.assertTrue(day04.is_password_valid_v2('112233'))
        self.assertTrue(day04.is_password_valid_v2('111122'))
        self.assertFalse(day04.is_password_valid_v2('123444'))
if __name__ == "__main__":
    unittest.main()