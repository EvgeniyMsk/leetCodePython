import unittest
import Solution


solution = Solution.Solution()


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution.findTheWinner(5, 2), 3)

    def test_2(self):
        self.assertEqual(solution.findTheWinner(6, 5), 1)