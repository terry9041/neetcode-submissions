# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # T: O(n+m)
        # S: O(n+m) for call stack height of n+m
        # we need to reassign l1 or l2 next we are trying to relink it 
        # but there is no action before returning if we dont actually reassign
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2

        # # T: O(n+m)
        # # S: O(1) no call stack
        # dummy = ListNode()
        # tail = dummy
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         tail.next = list1
        #         list1 = list1.next
        #     else:
        #         tail.next = list2
        #         list2 = list2.next
        #     tail = tail.next
        # if list1:
        #     tail.next = list1
        # if list2:
        #     tail.next = list2
        # return dummy.next