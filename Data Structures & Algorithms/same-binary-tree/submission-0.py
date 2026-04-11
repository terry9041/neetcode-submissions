# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # TC: O(min(N,M)), where N,M is the num of nodes for p,q
        # SC: O(min(H1,H2)), where H1, H2 is the tree height for p,q
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)) 