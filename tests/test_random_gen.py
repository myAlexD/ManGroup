import unittest
from src.random_gen import RandomGen

class TestRandomGen(unittest.TestCase):
    def setUp(self):
        self._random_nums = [-1, 0, 1, 2, 3]
        self._probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]

    def test_probabilities_sum(self):
        self.assertRaises(ValueError, RandomGen, self._random_nums, [0.1, 0.2])

    def test_random_output(self):
        rng = RandomGen(self._random_nums, self._probabilities)
        for _ in range(100):
            self.assertIn(rng.next_num(), self._random_nums)

if __name__ == '__main__':
    unittest.main()
