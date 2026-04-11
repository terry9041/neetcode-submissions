# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        curr = root
        prev = -1001

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            print([node.val for node in stack])
            curr = stack.pop()
            if curr.val <= prev:
                return False
            prev = curr.val
            curr = curr.right

        return True
            