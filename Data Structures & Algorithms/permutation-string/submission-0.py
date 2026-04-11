from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        freq2 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        for i in range(len(s1)):
            freq1[s1[i]] += 1
        i = 0

        for j in range(len(s2)):
            if freq1[s2[j]] == 0: #char not in s1
            # we undo the increment for the char on i <= x < j
            # then we move i to j+1
                for x in range(i,j):
                    freq2[s2[x]] -= 1
                i = j + 1
            else:
                # else we increment for the char    
                freq2[s2[j]] += 1

                while (j-i+1) > len(s1):
                    freq2[s2[i]] -= 1
                    i += 1

                if (freq1 == freq2):
                    return True
        return False





                