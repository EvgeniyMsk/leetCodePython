import unittest
import Solution

solution = Solution.Solution()

class TestTask26(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution.removeDuplicates([1, 1, 2]), 2)

    def test_1(self):
        self.assertEqual(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
