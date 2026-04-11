from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        freq = defaultdict(int)
        maxFreq = 0
        res = 0
        for j in range(len(s)):
            freq[s[j]] += 1

            maxFreq = max(maxFreq,freq[s[j]])

            if (j-i+1)-maxFreq > k:
                freq[s[i]] -=1
                i += 1
                temp = 0
                for key,val in freq.items():
                    temp = max(temp,val)
                maxFreq = temp

            res = max(res, (j-i+1))
        return res
            

