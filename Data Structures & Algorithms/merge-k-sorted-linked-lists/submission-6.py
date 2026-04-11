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
        
        # 2. divide and conquer
        while len(lists) > 1:
            merged_pairs = []
            for i in range(0, len(lists), 2):
                # append the merge res of two lists, 
                # also take care of case if there is no "next
                merged_pairs.append(merge(lists[i], lists[i+1] if (i+1)<len(lists) else None))
            lists = merged_pairs
        
        return lists[0]

        # TC: O(nlogk) where n is total num of nodes, k is num of lists
        # SC: O(k) for merged_pairs, not O(n) as we are relinking old nodes, not creating new nodes