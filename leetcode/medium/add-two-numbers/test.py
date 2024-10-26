import unittest
from main2 import Solution, ListNode


class TestSolution(unittest.TestCase):
    """
    Entrada: l1 = [2,4,3], l2 = [5,6,4]
    Saída: [7,0,8]
    Explicação: 342 + 465 = 807.
    Exemplo 2:

    Entrada: l1 = [0], l2 = [0]
    Saída: [0]
    Exemplo 3:

    Entrada: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Saída: [8,9,9,9,0,0,0,1]
    """

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 8)

    def test_example_two(self):
        l1 = ListNode(0)
        l2 = ListNode(0)
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(result.val, 0)

    def test_example_three(self):
        l1 = ListNode(
            9,
            ListNode(
                9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
            ),
        )
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(result.val, 8)
        self.assertEqual(result.next.val, 9)
        self.assertEqual(result.next.next.val, 9)
        self.assertEqual(result.next.next.next.val, 9)
        self.assertEqual(result.next.next.next.next.val, 0)
        self.assertEqual(result.next.next.next.next.next.val, 0)
        self.assertEqual(result.next.next.next.next.next.next.val, 0)
        self.assertEqual(result.next.next.next.next.next.next.next.val, 1)

    def test_exanple_four(self):
        l1 = ListNode(5)
        l2 = ListNode(5)
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(result.val, 0)
        self.assertEqual(result.next.val, 1)
