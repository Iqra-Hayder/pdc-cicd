import unittest

from app import parallel_sum_of_squares, square


class TestApp(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(4), 16)

    def test_parallel_sum_small(self):
        self.assertEqual(parallel_sum_of_squares([1, 2, 3], workers=2), 14)

    def test_parallel_sum_matches_serial(self):
        data = list(range(1, 101))
        expected = sum(n * n for n in data)
        self.assertEqual(parallel_sum_of_squares(data, workers=4), expected)


if __name__ == "__main__":
    unittest.main()
