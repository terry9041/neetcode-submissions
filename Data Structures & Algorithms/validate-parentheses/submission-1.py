class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {"[":"]","{":"}","(":")"}
        for i in range(len(s)):
            if s[i] in hashmap: # if it is LHS
                stack.append(s[i])
            else: # if it is RHS
                if len(stack) ==0:
                    return False
                if hashmap[stack[-1]] == s[i]:
                    stack.pop(-1)
                else:
                    return False
        return len(stack) ==0
