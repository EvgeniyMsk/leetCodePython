import unittest
import Solution

solution = Solution.Solution()

class Tests(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solution.reverseParentheses("(abcd)"), "dcba")

    def test_case2(self):
        self.assertEqual(solution.reverseParentheses("(u(love)i)"), "iloveu")

    def test_case3(self):
        self.assertEqual(solution.reverseParentheses("(ed(et(oc))el)"), "leetcode")