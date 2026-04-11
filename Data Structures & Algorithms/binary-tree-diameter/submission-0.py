# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS
        # diameter = L+R subtree treeheight
        # return treeheight at the end for calculating its parent
        # set up global var

        # TC: O(n), n = num of nodes
        # SC: O(n), n = tree height
        maxDiameter = [0]
        def DFS(root):
            if not root:
                return 0
            t1 = DFS(root.left)
            t2 = DFS(root.right)
            diameter = t1 + t2
            maxDiameter[0] = max(maxDiameter[0], diameter)
            return 1+max(t1,t2)
        DFS(root)
        return maxDiameter[0]
            