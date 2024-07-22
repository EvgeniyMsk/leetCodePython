import unittest
import Solution

solution = Solution.Solution()


class Tests(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(1, solution.climbStairs(1))

    def test_case2(self):
        self.assertEqual(2, solution.climbStairs(2))

    def test_case3(self):
        self.assertEqual(3, solution.climbStairs(3))

    def test_case4(self):
        self.assertEqual(5, solution.climbStairs(4))
