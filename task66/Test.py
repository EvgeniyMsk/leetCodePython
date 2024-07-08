import unittest
import Solution

solution = Solution.Solution()


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution.plusOne([1, 2, 3]), [1, 2, 4])

    def test_2(self):
        self.assertEqual(solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_3(self):
        self.assertEqual(solution.plusOne([9]), [1, 0])