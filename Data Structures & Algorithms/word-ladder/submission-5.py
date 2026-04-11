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
                if word == endWord:
                    return steps
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:] 
                    for neighbour in adList[pattern]:
                        if neighbour == endWord:
                            return steps + 1
                        elif neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)
            steps += 1
        return 0


