class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l3: ListNode = ListNode()
        list3: ListNode = l3

        while list3 != l1 and list3 != l2:
            list3.val = list3.val + l1.val + l2.val

            if l1.next != None and l2.next != None:
                node: ListNode = ListNode()
                list3.next = node

            else:
                if l1.next != None:
                    list3.next = l1.next
                elif l2.next != None:
                    list3.next = l2.next
                elif list3.val >= 10:
                    node: ListNode = ListNode()
                    list3.next = node
                    list3.next.val += 1
                    list3.val -= 10
                    break

            if list3.val >= 10:
                list3.next.val += 1
                list3.val -= 10

            l1 = l1.next
            l2 = l2.next
            list3 = list3.next

        while list3 != None:
            if list3.val >= 10:
                if list3.next == None:
                    node: ListNode = ListNode()
                    list3.next = node
                list3.next.val += 1
                list3.val -= 10
                list3 = list3.next
            else:
                return l3

        return l3
