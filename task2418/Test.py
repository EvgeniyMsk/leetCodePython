import unittest
import Solution

solution = Solution.Solution()


class Tests(unittest.TestCase):
    def test_case1(self):
        names = ["Mary", "John", "Emma"]
        heights = [180, 165, 170]
        self.assertEqual(["Mary", "Emma", "John"], solution.sortPeople(names, heights))

    def test_case2(self):
        names = ["Alice", "Bob", "Bob"]
        heights = [155, 185, 150]
        self.assertEqual(["Bob", "Alice", "Bob"], solution.sortPeople(names, heights))
