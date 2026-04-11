# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.index = 0

        def helper(start, end):
            print(start, end, self.index)
            if start > end:
                return None

            # pick the current root from preorder
            root = TreeNode(preorder[self.index])
            self.index += 1

            # find the split in inorder
            mid = idx_map[root.val]

            # assign left then assign right
            root.left = helper(start, mid-1)
            root.right = helper(mid+1, end)

            return root

        return helper(0, len(inorder)-1)

        # TC: O(n), check every single node / hashmap creation
        # SC: O(n) for the hashmap

