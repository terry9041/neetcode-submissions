class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        i = 0
        maxLen = 0
        for j in range(len(s)):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1
            maxLen = max(maxLen, j-i+1)
            char_set.add(s[j])
        return maxLen
            