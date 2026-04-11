class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(s, open, close):
            if open == close and open == n:
                res.append(s)
            if open < n:
                dfs(s + "(", open + 1, close)
            if close < n and open > close:
                dfs(s + ")", open, close + 1)
        dfs("", 0, 0)
        return res
        