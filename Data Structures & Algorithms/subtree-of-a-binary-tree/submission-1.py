# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if root == None and subRoot != None:
        #     return False
        # if root == None and subRoot == None:
        #     return True
        # if (root.val == subRoot.val):
        #     return self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)
        # else:
        #     return self.isSubtree(root.left, subRoot.left) or self.isSubtree(root.right, subRoot.right)

        # above is wrong as it mixed up checking if current root contains the subtree and doing that for left and right
        # we cannot use isSubtree to compare left of root and left or subroot

        # correct approach
        def isSameTree(p,q):
            if (p==q) and p == None:
                return True
            if (p!=q) and (p==None or q == None):
                return False
            return (p.val == q.val) and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        if not root:
            return False # as empty tree cannot contain any non-empty subtree
        else:
            if isSameTree(root,subRoot):
                return True # since we found the right tree at current root node
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        # takeaway:
        # 1. read quesitons carefully
        #     eg non empty? non negative? -> types of check required
        #     eg binary tree can have duplicates, but not binary search tree
        # 2. break down the problems in simpler terms, use helper func if needed
        #     eg check if currnet is subtree, if not, check left and right
        #     -> can we make a helper func to do the check?
        #      -> if yes, which funciton should we call to make the recursion work?
        #       -> call the og function for recursion, call helper for check
