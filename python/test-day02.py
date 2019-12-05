import unittest
from . import computer

# ALL TESTS HAVE BEEN MOVED TO test-computer.py

class TestDay2(unittest.TestCase):
    def test_operators_are_split_correctly(self):
        test_array = [1, 5, 6, 3, 0, 10, 20]
        expected_result = [1, 5, 6, 3, 0]
        expected_refactored_result = {
            'opcode': expected_result[0],
            'parameters': expected_result[1:4],
            'parameter_modes': [0,0,0],
            'index_of_opcode': expected_result[4]
        }
        self.assertEqual(computer.getNextOperationMembers(test_array), expected_refactored_result)
if __name__ == "__main__":
    unittest.main()