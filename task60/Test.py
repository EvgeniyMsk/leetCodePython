import unittest
import Solution

solution = Solution.Solution()


class TestTask60(unittest.TestCase):


    def test_1(self):
        self.assertEqual(solution.getPermutation(3, 3), "213")

    def test_2(self):
        self.assertEqual(solution.getPermutation(4, 9), "2314")

    def test_3(self):
        self.assertEqual(solution.getPermutation(3, 1), "123")

    def test_4(self):
        print(solution.getPermutation(5, 35))
