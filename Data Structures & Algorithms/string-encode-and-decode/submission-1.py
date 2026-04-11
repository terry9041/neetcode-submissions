class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for s in strs:
            msg += str(len(s))
            msg += "#"
            msg += s
        return msg

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            length = 0
            while s[i] != "#":
                length *= 10
                length += int(s[i])
                i += 1
            words.append(s[i+1:i+1+length])
            i += length + 1
        return words
