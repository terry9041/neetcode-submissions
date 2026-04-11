from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adList = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                wildCard = word[:i] + "*" + word[i+1:] 
                adList[wildCard].append(word)       
        
        visited = set([beginWord])
        queue = deque([beginWord])
        steps = 1
    
        while queue:
            lvl_size = len(queue)
            for _ in range(lvl_size):
                word = queue.popleft()
                for i in range(len(word)):
                    wildCard = word[:i] + "*" + word[i+1:] 
                    for next in adList[wildCard]:
                        if next == endWord:
                            return steps + 1
                        elif next not in visited:
                            visited.add(next)
                            queue.append(next)
                    adList[wildCard] = []
            steps += 1
        return 0


