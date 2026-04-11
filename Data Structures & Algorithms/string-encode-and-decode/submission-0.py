class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string))
            res += "¥"
            res += string
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        ptr = 0
        while ptr != len(s):
            wordLen = 0
            while s[ptr] != "¥":
                wordLen *= 10
                wordLen += int(s[ptr])
                ptr += 1
            ptr += 1
            res.append(s[ptr:ptr+wordLen])
            ptr += wordLen
        return res
            

