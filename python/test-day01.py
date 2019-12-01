import unittest
from . import day01

class TestDay1(unittest.TestCase):
    def test_basic(self):
        self.assertEqual('hello', 'hello')

    def test_fuel_is_calculated_correctly_for_given_examples(self):
        self.assertEqual(day01.get_fuel_required(module_mass=12), 2)
        self.assertEqual(day01.get_fuel_required(module_mass=14), 2)
        self.assertEqual(day01.get_fuel_required(module_mass=1969), 654)
        self.assertEqual(day01.get_fuel_required(module_mass=100756), 33583)

    def test_fuel_for_fuel_is_calculated_correctly_for_given_examples(self):
        self.assertEqual(day01.get_fuel_required_for_fuel(fuel_volume=2), 0)
        self.assertEqual(day01.get_fuel_required_for_fuel(fuel_volume=654), 966-654)
        self.assertEqual(day01.get_fuel_required_for_fuel(fuel_volume=33583), 50346-33583)
if __name__ == "__main__":
    unittest.main()