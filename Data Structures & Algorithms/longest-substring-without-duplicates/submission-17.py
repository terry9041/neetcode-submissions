class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0

        l = 0

        for r in range(len(s)):
            # increment L if needed to ensure valid window
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            # update max
            res = max(res, (r-l+1))
            # add R to seen for the next increment of R
            seen.add(s[r])
        
        return res
