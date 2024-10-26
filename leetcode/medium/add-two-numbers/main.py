class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry: int = 0
        start: ListNode = ListNode
        result: ListNode = start

        while l1 or l2:
            val1: int = l1.val if l1 else 0
            val2: int = l2.val if l2 else 0

            total: int = val1 + val2 + carry
            carry = total // 10

            result.next = ListNode(total % 10)
            result = result.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if not l1 and not l2 and carry != 0:
                result.next = ListNode(carry)

        return start.next
