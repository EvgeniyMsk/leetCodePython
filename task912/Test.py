import unittest
import Solution

solution = Solution.Solution()

class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution.sortArray([5, 2, 3, 1]), [1, 2, 3, 5])

    def test_2(self):
        self.assertEqual(solution.sortArray([5, 1, 1, 2, 0, 0]), [0, 0, 1, 1, 2, 5])

    def test_3(self):
        self.assertEqual(solution.sortArray([3, -1]), [-1, 3])
