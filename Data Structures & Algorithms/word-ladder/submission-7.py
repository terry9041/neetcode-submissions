from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 1

        matchMap = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                matchMap[key].append(word)
        
        res = 1

        queue = deque([beginWord])
        visited = set([beginWord])

        while queue:
            lvl_size = len(queue)
            for _ in range(lvl_size):
                word = queue.popleft()
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neighbour in matchMap[pattern]:
                        if neighbour == endWord:
                            return res + 1
                        queue.append(neighbour)
                    matchMap[pattern] = []
            res += 1
        
        return 0

        