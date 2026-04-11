from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adList = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:] 
                adList[pattern].append(word)       
        
        visited = {beginWord}
        queue = deque([beginWord])
        steps = 1
    
        while queue:
            lvl_size = len(queue)
            for _ in range(lvl_size):
                word = queue.popleft()
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:] 
                    for next in adList[pattern]:
                        if next == endWord:
                            return steps + 1
                        elif next not in visited:
                            visited.add(next)
                            queue.append(next)
                    adList[pattern] = []
            steps += 1
        return 0


