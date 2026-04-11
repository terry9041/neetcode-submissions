# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            dummy = ListNode()
            curr = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            return dummy.next

        # 1. edge case check
        if not lists or len(lists) == 0:
            return None
        
        # 2. merge list at k, k-1 to k 
        for i in range(1, len(lists)):
            lists[i] = merge(lists[i], lists[i-1])
        
        return lists[-1]

        # TC: O(nk) to process n nodes for k times
        # SC: O(1) as everything is inplace