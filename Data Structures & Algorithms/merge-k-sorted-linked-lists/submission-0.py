# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = []
        for head in lists:
            while head:
                temp.append(head.val)
                head = head.next
        temp.sort()
        dummy = ListNode()
        curr = dummy
        for i in range(len(temp)):
            curr.next = ListNode(temp[i])
            curr = curr.next
        return dummy.next