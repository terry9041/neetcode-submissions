# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root,1)])
        res = []

        while queue:
            curr = queue.popleft()
            if curr[0]:
                if curr[1] > len(res):
                    res.append([])
                res[curr[1]-1].append(curr[0].val)
                queue.append((curr[0].left,curr[1]+1))
                queue.append((curr[0].right,curr[1]+1))
        
        return res
