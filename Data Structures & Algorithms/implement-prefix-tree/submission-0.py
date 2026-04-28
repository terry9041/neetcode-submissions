class TrieNode:
    def __init__(self):
        self.children = [0] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            # calculate pos
            pos = ord(word[i]) - ord("a")
            # check if it is marked, if not mark it
            if curr.children[pos] == 0: 
                curr.children[pos] = TrieNode()
            # check if it is last char, if yes mark it
            if i == (len(word)-1):
                curr.children[pos].endOfWord = True
            # increment curr
            curr = curr.children[pos]
            
    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            pos = ord(word[i]) - ord("a")
            if curr.children[pos] == 0:
                return False
            curr = curr.children[pos]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            pos = ord(prefix[i]) - ord("a")
            if curr.children[pos] == 0:
                return False
            curr = curr.children[pos]
        return True


        
        