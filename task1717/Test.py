import unittest
import Solution

solution = Solution.Solution()

class Tests(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(19, solution.maximumGain("cdbcbbaaabab", 4, 5))

    def test_case2(self):
        self.assertEqual(20, solution.maximumGain("aabbaaxybbaabb", 5, 3))