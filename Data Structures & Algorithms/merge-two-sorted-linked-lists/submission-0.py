# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
         # # T: O(n+m)
        # # S: O(n+m)
        if (list1 == None):
            return list2
        elif (list2 == None):
            return list1
        else:
            if (list1.val < list2.val):
                list1.next = self.mergeTwoLists(list1.next,list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list2.next,list1)
                return list2

        # # T: O(n+m)
        # # S: O(1)
        # # reason why we use dummy is that wt if both are empty
        # # in that case, we could just set early return, but look not as good
        # # and also that eliminates the hassle of assigning the first node
        # dummy = ListNode()
        # tail = dummy
        # while (list1 != None) and (list2 != None):
        #     if list1.val < list2.val:
        #         tail.next = list1
        #         list1 = list1.next
        #     else:
        #         tail.next= list2
        #         list2 = list2.next
        #     tail = tail.next
        # if (list1 == None):
        #     tail.next = list2
        # else:
        #     tail.next = list1
        # return dummy.next