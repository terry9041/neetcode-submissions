# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            # 1. set up v1 v2 for the summation
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # 2. calculate digit to append and the carry
            res = v1 + v2 + carry
            digit = res % 10
            carry = res // 10

            # 3. append new node and increment curr ptr
            curr.next = ListNode(digit)
            curr = curr.next

            # 4. increment l1, l2 accordingly
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next