class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. create adj list, char:set(char)
        adList = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adList[w1[j]].add(w2[j]) 
                    break

        # 2. setup
        visiting = set() # marked as visiting while on the path
        visited = set() # marked as visited after traversing its neighours and it's no cyclical

        res = []


        def dfs(c):
            # return False if in the path -> cyclic
            if c in visiting:
                return False 
            # return True if that node is safe already
            if c in visited:
                return True

            # add char to path before visiting neighbours
            visiting.add(c)

            # visit its neighbours, see if neighour is cyclic
            for neighbour in adList[c]:
                if not dfs(neighbour):
                    return False

            # post-order step
            visiting.remove(c)

            # add to non-cyclic list
            visited.add(c)

            res.append(c)

            return True

        for c in adList:
            if not dfs(c):
                return ""
        
        return "".join(res[::-1])

       


        