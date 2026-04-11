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
        queue = deque([root])

        while queue:
            # The rightmost elem is at the end of the current queue
            res.append(queue[0].val)

            # Set up next level of nodes
            # We add right first so that the rightmost elem always stays at end
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            
        return res

        # TC: O(N), N = number of node
        # SC: O(W), W = max width across all lvls




