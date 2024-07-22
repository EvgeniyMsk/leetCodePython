import unittest
import Solution

solution = Solution.Solution()


class TestSolution(unittest.TestCase):
    def test_solution1(self):
        self.assertEqual(solution.hammingWeight(11), 3)

    def test_solution2(self):
        self.assertEqual(solution.hammingWeight(128), 1)

    def test_solution3(self):
        self.assertEqual(solution.hammingWeight(2147483645), 30)
