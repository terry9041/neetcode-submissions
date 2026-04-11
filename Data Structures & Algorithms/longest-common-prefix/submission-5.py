class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        first = strs[0]

        for i in range(len(first)):
            for string in strs:
                if len(string) <= i or string[i] != first[i]:
                    return first[0:i]
        return first

        # i = 0, 1, 2
        # i = 0 => string = "abc", "", "abcd"
            