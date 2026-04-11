# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []

        # BFS
        queue = deque([root])

        # in the queue, we always keep track of the first elem to be the right side node
        # in short, we flip the tree horizontally for each lvl's nodes
        while queue:
            res.append(queue[0].val)

            # append right first
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        # TC: O(n) always the same as we process every node
        # SC: O(w) max width of the tree
            
        return res
