import unittest
from . import day05

class TestDay5(unittest.TestCase):
    def test_an_instruction_is_recognised_as_so(self):
        self.assertTrue(day05.is_instruction(1))
        self.assertTrue(day05.is_instruction(2))
        self.assertTrue(day05.is_instruction(3))
        self.assertTrue(day05.is_instruction(4))
        self.assertTrue(day05.is_instruction(99))
        self.assertTrue(day05.is_instruction(104))
        self.assertTrue(day05.is_instruction(1105))
        self.assertFalse(day05.is_instruction(100))
        self.assertFalse(day05.is_instruction(1204))
        self.assertFalse(day05.is_instruction(100004))
    def test_operators_are_split_correctly(self):
        test_array = [1, 5, 6, 3, 0, 10, 20]
        expected_result = [1, 5, 6, 3, 0]
        expected_refactored_result = {
            'opcode': expected_result[0],
            'parameters': expected_result[1:4],
            'parameter_modes': [0,0,0],
            'index_of_opcode': expected_result[4]
        }
        self.assertEqual(day05.getNextOperationMembers(test_array), expected_refactored_result)
        test_array = [2, 5, 6, 3, 0, 10, 20]
        expected_result = [2, 5, 6, 3, 0]
        expected_refactored_result = {
            'opcode': expected_result[0],
            'parameters': expected_result[1:4],
            'parameter_modes': [0,0,0],
            'index_of_opcode': expected_result[4]
        }
        self.assertEqual(day05.getNextOperationMembers(test_array), expected_refactored_result)
        test_array = [99, 5, 6, 3, 0, 10, 20]
        expected_result = [99, 0]
        expected_refactored_result = {
            'opcode': expected_result[0],
            'parameters': [],
            'parameter_modes': [0,0,0],
            'index_of_opcode': expected_result[1]
        }
        self.assertEqual(day05.getNextOperationMembers(test_array), expected_refactored_result)
        test_array = [33, 44, 2, 3, 0, 10, 20]
        expected_result = [2, 3, 0, 10, 2]
        expected_refactored_result = {
            'opcode': expected_result[0],
            'parameters': expected_result[1:4],
            'parameter_modes': [0,0,0],
            'index_of_opcode': expected_result[4]
        }
        self.assertEqual(day05.getNextOperationMembers(test_array), expected_refactored_result)
        test_array = [39, 22, 30, 99, 5, 6, 3, 0, 10, 20]
        expected_result = [99, 3]
        expected_refactored_result = {
            'opcode': expected_result[0],
            'parameters': [],
            'parameter_modes': [0,0,0],
            'index_of_opcode': expected_result[1]
        }
        self.assertEqual(day05.getNextOperationMembers(test_array), expected_refactored_result)
        
        test_array = [39, 22, 3, 50, 99, 5, 6, 3, 0, 10, 20]
        expected_refactored_result = {
            'opcode': 3,
            'parameters': [50],
            'parameter_modes': [0,0,0],
            'index_of_opcode': 2
        }
        self.assertEqual(day05.getNextOperationMembers(test_array), expected_refactored_result)
        test_array = [39, 22, 4, 50, 99, 5, 6, 3, 0, 10, 20]
        expected_refactored_result = {
            'opcode': 4,
            'parameters': [50],
            'parameter_modes': [0,0,0],
            'index_of_opcode': 2
        }
        self.assertEqual(day05.getNextOperationMembers(test_array), expected_refactored_result)
        test_array = [1002,4,3,4,33]
        expected_result = {
            'opcode': 2,
            'parameters': [4,3,4],
            'parameter_modes': [0,1,0],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.getNextOperationMembers(test_array), expected_result)

        test_array = [1005,4,3,4,33]
        expected_result = {
            'opcode': 5,
            'parameters': [4, 3],
            'parameter_modes': [0,1,0],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.getNextOperationMembers(test_array), expected_result)

        test_array = [1006,4,3,4,33]
        expected_result = {
            'opcode': 6,
            'parameters': [4, 3],
            'parameter_modes': [0,1,0],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.getNextOperationMembers(test_array), expected_result)

        test_array = [1007,4,3,4,33]
        expected_result = {
            'opcode': 7,
            'parameters': [4, 3, 4],
            'parameter_modes': [0,1,0],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.getNextOperationMembers(test_array), expected_result)

        test_array = [1008,4,3,4,33]
        expected_result = {
            'opcode': 8,
            'parameters': [4, 3, 4],
            'parameter_modes': [0,1,0],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.getNextOperationMembers(test_array), expected_result)

    def test_numbers_are_read_and_added_correctly(self):
        test_array = [1, 5, 6, 3, 0, 10, 20]
        operation_specification = {
            'opcode': 1,
            'parameters': [5,6,3],
            'parameter_modes': [0,0,0],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.executeOperation(operation_specification, test_array), 30)

    def test_numbers_are_read_and_multiplied_correctly(self):
        test_array = [2, 5, 6, 3, 0, 10, 20]
        operation_specification = {
            'opcode': 2,
            'parameters': [5,6,3],
            'parameter_modes': [0,0,0],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.executeOperation(operation_specification, test_array), 200)

    def test_operation_receives_none_on_99(self):
        test_array = [2, 5, 6, 3, 99, 10, 20]
        operation_specification = {
            'opcode': 99,
            'parameters': [],
            'parameter_modes': [0,0,0],
            'index_of_opcode': 0
        }
        self.assertIsNone(day05.executeOperation(operation_specification, test_array))

    def atest_number_is_read_and_stored_correctly(self):
        test_array = [3,2,21,99]
        operation_specification = {
            'opcode': 3,
            'parameters': [2],
            'parameter_modes': [0,0,0],
            'index_of_opcode': 0
        }
        print('when asked to give input, give an input of 30')
        self.assertEqual(day05.executeOperation(operation_specification, test_array), 30)

    def test_opcode_four_outputs_number_in_position(self):
        test_array = [4,2,21,99]
        operation_specification = {
            'opcode': 4,
            'parameters': [2],
            'parameter_modes': [0,0,0],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.executeOperation(operation_specification, test_array), 21)

    def test_opcode_five_returns_jump_value_correctly(self):
        test_array = [1105, 20, 4, 1, 2, 3, 3, 99]
        operation_specification = {
            'opcode': 5,
            'parameters': [20, 4],
            'parameter_modes': [0,1,1],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.executeOperation(operation_specification, test_array), 4)
        test_array = [105, 20, 4, 1, 2, 3, 3, 99]
        operation_specification = {
            'opcode': 5,
            'parameters': [20, 4],
            'parameter_modes': [0,0,1],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.executeOperation(operation_specification, test_array), 2)
        test_array = [5, 2, 4, 1, 2, 3, 3, 99]
        operation_specification = {
            'opcode': 5,
            'parameters': [2, 4],
            'parameter_modes': [0,0,0],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.executeOperation(operation_specification, test_array), 2)
        test_array = [5, 4, 5, 1, 0, 3, 3, 99]
        operation_specification = {
            'opcode': 5,
            'parameters': [4, 5],
            'parameter_modes': [0,0,0],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.executeOperation(operation_specification, test_array), -1)

    def test_opcode_six_returns_jump_value_correctly(self):
        test_array = [1106, 0, 4, 1, 2, 3, 3, 99]
        operation_specification = {
            'opcode': 6,
            'parameters': [0, 4],
            'parameter_modes': [0,1,1],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.executeOperation(operation_specification, test_array), 4)
        test_array = [106, 0, 4, 1, 2, 3, 3, 99]
        operation_specification = {
            'opcode': 6,
            'parameters': [0, 4],
            'parameter_modes': [0,0,1],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.executeOperation(operation_specification, test_array), 2)
        test_array = [6, 3, 4, 0, 2, 3, 3, 99]
        operation_specification = {
            'opcode': 6,
            'parameters': [3, 4],
            'parameter_modes': [0,0,0],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.executeOperation(operation_specification, test_array), 2)
        test_array = [6, 4, 5, 1, 4, 3, 3, 99]
        operation_specification = {
            'opcode': 6,
            'parameters': [4, 5],
            'parameter_modes': [0,0,0],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.executeOperation(operation_specification, test_array), -1)

    def test_opcode_seven_returns_value_to_store_correctly(self):
        test_array = [7, 4, 5, 7, 4, 5, 99, 10]
        operation_specification = {
            'opcode': 7,
            'parameters': [4, 5, 7],
            'parameter_modes': [0,0,0],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.executeOperation(operation_specification, test_array), 1)
        test_array = [7, 5, 4, 7, 4, 5, 99, 10]
        operation_specification = {
            'opcode': 7,
            'parameters': [5, 4, 7],
            'parameter_modes': [0,0,0],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.executeOperation(operation_specification, test_array), 0)
    def test_opcode_eight_returns_value_to_store_correctly(self):
        test_array = [8, 2, 3, 7, 4, 5, 99, 10]
        operation_specification = {
            'opcode': 8,
            'parameters': [2, 3, 7],
            'parameter_modes': [0,0,0],
            'index_of_opcode': 0
        }
        self.assertEqual(day05.executeOperation(operation_specification, test_array), 0)
    def test_full_operation_runs_on_array(self):
        test_array = [1,9,10,3,2,3,11,0,99,30,40,50]
        expected_result = [3500,9,10,70,2,3,11,0,99,30,40,50]
        result_received, _ = day05.run_program(test_array) 
        self.assertEqual(result_received, expected_result)
        test_array = [1002,4,3,4,33]
        expected_result = [1002,4,3,4,99]
        result_received, _ = day05.run_program(test_array) 
        self.assertEqual(result_received, expected_result)
    def test_operations_work_with_input_required(self):
        test_array = [int(c) for c in '3,9,8,9,10,9,4,9,99,-1,8'.split(',')]
        print("Input 8")
        _, result_received = day05.run_program(test_array)
        self.assertEqual(result_received[-1], 1)
        test_array = [int(c) for c in '3,9,8,9,10,9,4,9,99,-1,8'.split(',')]
        print("Input a number that is not 8")
        _, result_received = day05.run_program(test_array)
        self.assertEqual(result_received[-1], 0)

        test_array = [int(c) for c in '3,9,7,9,10,9,4,9,99,-1,8'.split(',')]
        print("Input a number less than 8")
        _, result_received = day05.run_program(test_array)
        self.assertEqual(result_received[-1], 1)
        test_array = [int(c) for c in '3,9,7,9,10,9,4,9,99,-1,8'.split(',')]
        print("Input 8")
        _, result_received = day05.run_program(test_array)
        self.assertEqual(result_received[-1], 0)

        test_array = [int(c) for c in '3,3,1108,-1,8,3,4,3,99'.split(',')]
        print("Input 8")
        _, result_received = day05.run_program(test_array)
        self.assertEqual(result_received[-1], 1)
        test_array = [int(c) for c in '3,3,1108,-1,8,3,4,3,99'.split(',')]
        print("Input a number that is not 8")
        _, result_received = day05.run_program(test_array)
        self.assertEqual(result_received[-1], 0)

        test_array = [int(c) for c in '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'.split(',')]
        print("Input a non 0 number")
        _, result_received = day05.run_program(test_array)
        self.assertEqual(result_received[-1], 1)
        test_array = [int(c) for c in '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'.split(',')]
        print("Input 0")
        _, result_received = day05.run_program(test_array)
        self.assertEqual(result_received[-1], 0)

if __name__ == "__main__":
    unittest.main()