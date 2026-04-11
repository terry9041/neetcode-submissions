class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []

        def backtrack(path, pos):
            # base case
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            # go thro each possible letter for that digit as choices
            for char in mapping[digits[pos]]:
                path.append(char)
                backtrack(path, pos + 1)
                path.pop()

        backtrack([],0)
        return res
