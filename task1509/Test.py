import unittest
import Solution


solution = Solution.Solution()

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution.minDifference([5, 3, 2, 4]), 0)

    def test_2(self):
        self.assertEqual(solution.minDifference([1, 5, 0, 10, 14]), 1)

    def test_3(self):
        self.assertEqual(solution.minDifference([3, 100, 20]), 0)
