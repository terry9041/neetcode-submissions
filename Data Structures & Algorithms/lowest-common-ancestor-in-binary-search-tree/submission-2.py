# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # root is always a valid CA
        lca = root

        if p.val > q.val:
            p, q = q, p

        while lca:
            if lca.val < p.val:
                lca = lca.right
            elif lca.val > q.val:
                lca = lca.left
            else:
                return lca
            
