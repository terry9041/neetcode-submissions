class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(curr, j):
            if j == len(word):
                return curr.endOfWord
            
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(child, i +1):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    return dfs(curr.children[c], j +1)

        return dfs(self.root, 0)
            

