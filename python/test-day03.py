import unittest
from . import day03

class TestDay3(unittest.TestCase):
    def test_manhattan_distance_is_calculated_correctly(self):
        self.assertTrue(True)

    def test_list_of_points_can_be_obtained_from_an_instruction(self):
        instruction = 'R2'
        starting_coordinates = (0,0)
        expected_result = [(1,0), (2,0)]
        returned_result = day03.get_points_from_current_position_to_next(instruction=instruction, starting_coordinates=starting_coordinates)
        self.assertEqual(returned_result, expected_result)

        instruction = 'U2'
        starting_coordinates = (0,0)
        expected_result = [(0,1), (0,2)]
        returned_result = day03.get_points_from_current_position_to_next(instruction=instruction, starting_coordinates=starting_coordinates)
        self.assertEqual(returned_result, expected_result)

        instruction = 'L4'
        starting_coordinates = (2,7)
        expected_result = [(1,7), (0,7), (-1,7), (-2,7)]
        returned_result = day03.get_points_from_current_position_to_next(instruction=instruction, starting_coordinates=starting_coordinates)
        self.assertEqual(returned_result, expected_result)

        instruction = 'D3'
        starting_coordinates = (3,-5)
        expected_result = [(3,-6), (3,-7), (3,-8)]
        returned_result = day03.get_points_from_current_position_to_next(instruction=instruction, starting_coordinates=starting_coordinates)
        self.assertEqual(returned_result, expected_result)

    def test_list_of_points_can_be_obtained_from_full_instruction_set(self):
        instruction_list = ['R2', 'U2', 'L4', 'D3']
        expected_result = [
            (1,0),
            (2,0),
            (2,1),
            (2,2),
            (1,2),
            (0,2),
            (-1,2),
            (-2,2),
            (-2,1),
            (-2,0),
            (-2,-1)
        ]
        returned_result = day03.get_points_for_given_instruction_set(instruction_list=instruction_list)
        self.assertEqual(returned_result, expected_result)

    def test_intersections_of_two_wires_can_be_found(self):
        instruction_list_A = 'R8,U5,L5,D3'.split(',')
        instruction_list_B = 'U7,R6,D4,L4'.split(',')
        intersection_points = day03.get_intersection_points_for_wires(instruction_list_A, instruction_list_B)
        self.assertTrue((3,3) in intersection_points)
        self.assertTrue((6,5) in intersection_points)
        self.assertEqual(len(intersection_points), 2)

    def test_smallest_manhattan_distance_can_be_found_for_two_wire_paths(self):
        instruction_list_A = 'R8,U5,L5,D3'.split(',')
        instruction_list_B = 'U7,R6,D4,L4'.split(',')
        self.assertEqual(day03.find_smallest_manhattan_distance(instruction_list_A, instruction_list_B), 6)
        instruction_list_A = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
        instruction_list_B = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
        self.assertEqual(day03.find_smallest_manhattan_distance(instruction_list_A, instruction_list_B), 159)
        instruction_list_A = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')
        instruction_list_B = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')
        self.assertEqual(day03.find_smallest_manhattan_distance(instruction_list_A, instruction_list_B), 135)

if __name__ == "__main__":
    unittest.main()