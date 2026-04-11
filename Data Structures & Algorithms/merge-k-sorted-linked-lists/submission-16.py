# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # naive: loop to collect all nums in a list, sort them and return them on a new linked list
        # assume k = total no of nodes, n = list length
        # TC: O(klogk), k to collect, klogk for sort, k to create new linked list
        # SC: O(k), the new res array

        # optimized: merge in pairs of two till one linked list left
        # TC: O(klogn), log n amount of layer, each layer require going thro every node
        # SC: O(k), extra space to store the temp list every time
        # OR we could do in-place merge on the linked list -> O(1)

        if len(lists) == 0:
            return None

        def merge(l1,l2):
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
            curr.next = l1 if l1 else l2
            return dummy.next
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged_lists.append(merge(l1, l2))
            lists = merged_lists
        
        return lists[0]

            
             