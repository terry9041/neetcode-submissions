class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = set()
        i = 0
        for j in range(len(s)):
            if s[j] not in seen:
                seen.add(s[j])
                res = max(res, len(seen))
                print(seen)
            else:   
                while s[j] in seen:
                    seen.remove(s[i])
                    i += 1
                seen.add(s[j])
        return res
