import unittest
import Solution

solution = Solution.Solution()


class Test(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(2, solution.searchInsert([1, 3, 5, 6], 5))

    def test_case_2(self):
        self.assertEqual(1, solution.searchInsert([1, 3, 5, 6], 2))

    def test_case_3(self):
        self.assertEqual(4, solution.searchInsert([1, 3, 5, 6], 7))

    def test_case_4(self):
        self.assertEqual(0, solution.searchInsert([1], 0))
