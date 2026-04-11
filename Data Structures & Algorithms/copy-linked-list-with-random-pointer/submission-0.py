"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {}

        dummy = Node(0)
        curr = dummy
        while head:
            if head not in mapping:
                node = Node(head.val)
                mapping[head] = node
            else:
                node = mapping[head]
            curr.next = node
            if not head.random:
                rand = None
            elif head.random not in mapping:
                rand = Node(head.random.val)
                mapping[head.random] = rand
            else:
                rand = mapping[head.random]
            curr.next.random = rand
            curr = curr.next
            head = head.next
        
        return dummy.next


