# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val < p.val:
            p,q = q,p
        curr = root
        while curr:
            if curr.val < p.val:
                curr = curr.right
            elif curr.val > q.val:
                curr = curr.left
            elif p.val <= curr.val <= q.val:
                return curr
            