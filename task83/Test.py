import unittest
import Solution
from task83.ListNode import ListNode

solution = Solution.Solution()


class TestSolution(unittest.TestCase):
    def test_solution_1(self):
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(3)

        solution.deleteDuplicates(head)
        while head != None:
            print(head.val)
            head = head.next

    def test_solution_2(self):
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(1)

        solution.deleteDuplicates(head)
        while head != None:
            print(head.val)
            head = head.next

    def test_solution_3(self):
        head = ListNode()

        solution.deleteDuplicates(head)
        while head != None:
            print(head.val)
            head = head.next
