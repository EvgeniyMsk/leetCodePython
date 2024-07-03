import unittest

import Solution

solution = Solution.Solution()


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution.firstMissingPositive([1, 2, 0]), 3)

    def test2(self):
        self.assertEqual(solution.firstMissingPositive([3, 4, -1, 1]), 2)

    def test3(self):
        self.assertEqual(solution.firstMissingPositive([7, 8, 9, 11, 12]), 1)
