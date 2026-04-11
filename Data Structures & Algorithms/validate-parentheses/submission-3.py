class Solution:
    def isValid(self, s: str) -> bool:
        # T: O(n) where n is the length of s
        # M: O(n), worst case: every symbol is LHS
        stack = []
        hashmap = {"{":"}","[":"]","(":")"}

        for char in s:
            # if its LHS
            if char in hashmap:
                stack.append(char)
            
            # else its RHS
            else:

                # no LHS to match, then False
                if len(stack) == 0:
                    return False

                # if the stack isnt empty, time to pop and check
                # if hashmap[poppedElem] = expecting RHS != actual RHS, then False
                else:
                    if hashmap[stack.pop(-1)] != char:
                        return False
        
        # if there is still unmatched LHS, return False
        return len(stack) == 0