# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # TC: O(n), n = num of nodes
        # SC: O(n), n = height of tree
        def DFS(root):
            if not root:
                return [True, 0]
            else:
                left = DFS(root.left)
                right = DFS(root.right)
                return [  left[0] and right[0] and abs(left[1]-right[1]) <= 1 , (1+max(left[1],right[1]))]
        return (DFS(root))[0]