import unittest
from . import computer

# ALL TESTS HAVE BEEN MOVED TO test-computer.py

class TestDay5(unittest.TestCase):
    def test_an_instruction_is_recognised_as_so(self):
        self.assertTrue(computer.is_instruction(104))

if __name__ == "__main__":
    unittest.main()