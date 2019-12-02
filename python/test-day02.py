import unittest
from . import day02

class TestDay2(unittest.TestCase):
    def test_operators_are_split_correctly(self):
        test_array = [1, 5, 6, 3, 0, 10, 20]
        expected_result = [1, 5, 6, 3, 0]
        self.assertEqual(day02.getNextOperationMembers(test_array), expected_result)
        test_array = [2, 5, 6, 3, 0, 10, 20]
        expected_result = [2, 5, 6, 3, 0]
        self.assertEqual(day02.getNextOperationMembers(test_array), expected_result)
        test_array = [99, 5, 6, 3, 0, 10, 20]
        expected_result = [99, 0]
        self.assertEqual(day02.getNextOperationMembers(test_array), expected_result)
        test_array = [33, 44, 2, 3, 0, 10, 20]
        expected_result = [2, 3, 0, 10, 2]
        self.assertEqual(day02.getNextOperationMembers(test_array), expected_result)
        test_array = [7, 22, 30, 99, 5, 6, 3, 0, 10, 20]
        expected_result = [99, 3]
        self.assertEqual(day02.getNextOperationMembers(test_array), expected_result)
        test_array = [7, 22, 30, 99, 5, 6, 3, 0, 10, 20]
        expected_result = [99, 3]
        self.assertEqual(day02.getNextOperationMembers(test_array), expected_result)
    def test_next_operation_array_is_generated_correctly(self):
        test_array = [1,9,10,3,2,3,11,0,99,30,40,50]
        self.assertEqual(day02.getNextOperationArray(test_array, 0), (test_array[:], 4))
        self.assertEqual(day02.getNextOperationArray(test_array, 4), (test_array[4:], 8))
        self.assertEqual(day02.getNextOperationArray(test_array, 8), (test_array[8:], 12))

    def test_numbers_are_read_and_added_correctly(self):
        test_array = [1, 5, 6, 3, 0, 10, 20]
        operation_specification = [1, 5, 6, 3, 0]
        self.assertEqual(day02.executeOperation(operation_specification, test_array), 30)

    def test_numbers_are_read_and_multiplied_correctly(self):
        test_array = [2, 5, 6, 3, 0, 10, 20]
        operation_specification = [2, 5, 6, 3, 0]
        self.assertEqual(day02.executeOperation(operation_specification, test_array), 200)

    def test_operation_receives_none_on_99(self):
        test_array = [2, 5, 6, 3, 99, 10, 20]
        operation_specification = [99, 0]
        self.assertIsNone(day02.executeOperation(operation_specification, test_array))

    def test_full_operation_runs_on_array(self):
        test_array = [1,9,10,3,2,3,11,0,99,30,40,50]
        expected_result = [3500,9,10,70,2,3,11,0,99,30,40,50]
        self.assertEqual(day02.run_program(test_array), expected_result)
if __name__ == "__main__":
    unittest.main()