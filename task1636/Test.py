import unittest
import Solution

solution = Solution.Solution()


class Tests(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solution.frequencySort([1, 1, 2, 2, 2, 3]), [3, 1, 1, 2, 2, 2])

    def test_case2(self):
        self.assertEqual(solution.frequencySort([2, 3, 1, 3, 2]), [1, 3, 3, 2, 2])

    def test_case3(self):
        self.assertEqual(solution.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]), [5, -1, 4, 4, -6, -6, 1, 1, 1])
