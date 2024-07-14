import unittest
import Solution

solution = Solution.Solution()

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution.countOfAtoms("H2O"), "H2O")

    def test_2(self):
        self.assertEqual(solution.countOfAtoms("Mg(OH)2"), "H2MgO2")

    def test_3(self):
        self.assertEqual(solution.countOfAtoms("K4(ON(SO3)2)2"), "K4N2O14S4")