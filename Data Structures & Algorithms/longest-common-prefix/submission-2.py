class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for string in strs:
                if len(string) <= i or string[i] != strs[0][i]:
                    return strs[0][0:i]
        return strs[0]

        # i = 0, 1, 2
        # i = 0 => string = "abc", "", "abcd"
            