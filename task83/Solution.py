from typing import Optional

import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if curr is None or curr.next is None:
            return head
        while curr.next.next is not None:
            next = curr.next
            while curr.val == curr.next.val and curr.val == next.val:
                next = curr.next.next
                curr.next = next
            curr = curr.next
        return head
