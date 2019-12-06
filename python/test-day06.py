import unittest
from . import day06

class TestDay6(unittest.TestCase):
    def test_orbits_dictionary_can_be_generated_correctly(self):
        test_array = ['COM)A',
        'A)B',
        'B)C']
        expected_result = {
            'COM': {'orbits': [], 'orbitted_by': ['A']},
            'A': {'orbits': ['COM'], 'orbitted_by': ['B']},
            'B': {'orbits': ['A'], 'orbitted_by': ['C']},
            'C': {'orbits': ['B'], 'orbitted_by': []},
        }
        self.assertEqual(day06.generate_orbit_map(test_array), expected_result)

        test_array = ['COM)A',
        'A)B',
        'B)C',
        'B)D']
        expected_result = {
            'COM': {'orbits': [], 'orbitted_by': ['A']},
            'A': {'orbits': ['COM'], 'orbitted_by': ['B']},
            'B': {'orbits': ['A'], 'orbitted_by': ['C', 'D']},
            'C': {'orbits': ['B'], 'orbitted_by': []},
            'D': {'orbits': ['B'], 'orbitted_by': []},
        }
        self.assertEqual(day06.generate_orbit_map(test_array), expected_result)

    def test_number_of_orbits_can_be_counted_for_a_given_object(self):
        orbit_map = {
            'COM': {'orbits': [], 'orbitted_by': ['A']},
            'A': {'orbits': ['COM'], 'orbitted_by': ['B']},
            'B': {'orbits': ['A'], 'orbitted_by': ['C', 'D']},
            'C': {'orbits': ['B'], 'orbitted_by': []},
            'D': {'orbits': ['B'], 'orbitted_by': []},
            'E': {'orbits': ['D'], 'orbitted_by': []}
        }
        self.assertEqual(day06.get_number_of_orbits_for_given_object('COM', orbit_map), 0)
        self.assertEqual(day06.get_number_of_orbits_for_given_object('A', orbit_map), 1)
        self.assertEqual(day06.get_number_of_orbits_for_given_object('B', orbit_map), 2)
        self.assertEqual(day06.get_number_of_orbits_for_given_object('C', orbit_map), 3)
        self.assertEqual(day06.get_number_of_orbits_for_given_object('D', orbit_map), 3)
        self.assertEqual(day06.get_number_of_orbits_for_given_object('E', orbit_map), 4)

    def test_total_number_of_orbits_can_be_found_for_a_given_orbit_map(self):
        orbit_map = {
            'COM': {'orbits': [], 'orbitted_by': ['A']},
            'A': {'orbits': ['COM'], 'orbitted_by': ['B']},
            'B': {'orbits': ['A'], 'orbitted_by': ['C', 'D']},
            'C': {'orbits': ['B'], 'orbitted_by': []},
            'D': {'orbits': ['B'], 'orbitted_by': []},
            'E': {'orbits': ['D'], 'orbitted_by': []}
        }
        self.assertEqual(day06.get_total_number_of_orbits(orbit_map), 13)
        orbit_map = day06.generate_orbit_map("""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""".split('\n'))
        self.assertEqual(day06.get_total_number_of_orbits(orbit_map), 42)

    def test_paths_can_be_found(self):
        orbit_map = day06.generate_orbit_map("""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN""".split('\n'))
        valid_paths = []
        self.assertEqual(day06.search_for_valid_path(orbit_map, 'YOU', 'SAN', 'YOU', [], valid_paths), ['YOU', 'K', 'J', 'E', 'D', 'I', 'SAN'])
        print(valid_paths)
if __name__ == "__main__":
    unittest.main()