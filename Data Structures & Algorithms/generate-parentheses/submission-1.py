class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, open, close):
            # base case
            if len(path) == n * 2:
                res.append("".join(path))
                return
            
            # explore options
            # 1. explore open if open < n:
            if open < n:
                path.append("(")
                backtrack(path, open+1, close)
                path.pop()
            
            # 2. explore close if open > close
            if open > close:
                path.append(")")
                backtrack(path, open, close +1)
                path.pop()

        backtrack([], 0, 0)
        return res

        # TC: O(4^n) upper bound
        # SC: O(n) max recursion depth