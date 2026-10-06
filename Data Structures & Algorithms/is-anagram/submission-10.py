

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap = {}
        for i in range(len(s)):
            if s[i] in hashMap:
                hashMap[s[i]] += 1
            else:
                hashMap[s[i]] = 1
            if t[i] in hashMap:
                hashMap[t[i]] -= 1
            else:
                hashMap[t[i]] = -1
        
        for char in hashMap:
            if hashMap[char] != 0:
                return False
        
        return True