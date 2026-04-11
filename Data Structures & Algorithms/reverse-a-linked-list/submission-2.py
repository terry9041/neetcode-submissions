# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # T: O(n)
        # # M: O(1)
        # prev, curr = None, head
        # while (curr != None):
        #     next = curr.next # save curr.next cuz we are about to change it to prev
        #     curr.next = prev # change the direction it is pointing to prev

        #     prev = curr # update prev to curr
        #     curr = next # update curr to next
        # return prev

        # T: O(n)
        # M: O(n) for max stack size of len(linkedList)

        def reverse (prev, curr):
            if curr == None:
                return prev
            else:
                next = curr.next
                curr.next = prev
                return reverse(curr, next)

        return reverse(None, head)