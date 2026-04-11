# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, parent):
            print(node.val if node else -1001, parent)
            if not node:
                return 
            if node.val >= parent:
                self.count += 1
            dfs(node.left, max(node.val, parent))
            dfs(node.right, max(node.val, parent))
        
        dfs(root, -101)
        return self.count

        