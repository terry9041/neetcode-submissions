class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def helper(curr, word, i):
            if i == (len(word)):
                return curr.endOfWord
            else:
                if word[i] == ".":
                    for child in curr.children:
                        if child and helper(child, word, i+1):
                            return True
                    return False
                else:
                    pos = ord(word[i]) - ord("a")
                    if curr.children[pos] == None:
                        return False
                    return helper(curr.children[pos], word, i+1)
        return helper(self.root, word, 0) 
            
            
