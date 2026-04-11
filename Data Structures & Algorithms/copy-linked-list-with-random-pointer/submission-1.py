class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        mapping = {}

        def get_copy(node):
            if not node:
                return None
            if node not in mapping:
                mapping[node] = Node(node.val)
            return mapping[node]
        
        curr = head
        while curr:
            copy = get_copy(curr)
            copy.random = get_copy(curr.random)
            copy.next = get_copy(curr.next)
            curr = curr.next
        
        return mapping[head]
            