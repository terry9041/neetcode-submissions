class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = dict()
        i = 0
        maxLen = 0
        for j in range(len(s)):
            while s[j] in hashmap:
                hashmap.pop(s[i])
                i += 1
            maxLen = max(maxLen, j-i+1)
            hashmap[s[j]] = j
        return maxLen
            