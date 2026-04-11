class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for c in s:
            if c == "(":
                low, high = low + 1, high + 1
            elif c == ")":
                low, high = low-1, high -1
            else:
                low, high = low-1, high+1
            
            low = 0 if low < 0 else low
            if high < 0:
                return False
        
        return low == 0
