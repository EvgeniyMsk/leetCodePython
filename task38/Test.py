import unittest
import Solution

solution = Solution.Solution()
class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution.countAndSay(1), "1")

    def test_2(self):
        self.assertEqual(solution.countAndSay(2), "11")

    def test_3(self):
        self.assertEqual(solution.countAndSay(3), "21")

    def test_4(self):
        self.assertEqual(solution.countAndSay(4), "1211")
