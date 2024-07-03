import unittest
import Solution

solution = Solution.Solution()


class TestTask58(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution.lengthOfLastWord("Hello World"), 5)

    def test_1(self):
        self.assertEqual(solution.lengthOfLastWord("   fly me   to   the moon  "), 4)

    def test_1(self):
        self.assertEqual(solution.lengthOfLastWord("luffy is still joyboy"), 6)
