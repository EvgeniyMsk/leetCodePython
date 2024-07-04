import unittest
import Solution

solution = Solution.Solution()

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution.removeElement([3, 2, 2, 3], 3), 2)

    def test_2(self):
        self.assertEqual(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)
