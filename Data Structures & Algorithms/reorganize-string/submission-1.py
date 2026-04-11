import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # BF: O(n!)
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)

        maxHeap = [[-count, char] for char, count in count.items() ]
        heapq.heapify(maxHeap)

        res = ""
        
        prev = None
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            count, char = heapq.heappop(maxHeap)
            res += char

            if prev:
                heapq.heappush(maxHeap,prev)
            
            prev = [count+1, char] if count+1 != 0 else None

        return res

        # TC: O(klogn) -> O(k)
        # SC: O(n) -> O(1)

        # n = num of unique char,capped at 26 , k = len of s



        # 1a2b2c4d
        # [-1, c], [-1, d]
        # 1: count, char = -4, d -> res = d -> prev = [-3,d] 
        # 2: count, char = -2, b -> res = db -> heappush([-3,d]) -> prev = -1,b
        # 3: count, char = -3, d -> res = dbd -> heappush([-1,b]) -> prev = -2,d
        # 4: count, char = -2, c -> res = dbdc -> heappush([-2,d]) -> prev = -1, c
        # 5: count, char = -2, d -> res = dbdcd -> heappush([-1,c]) -> prev = -1, d
        # 6: count, char = -1, a -> res = dbdcda -> heappush([-1,d]) -> prev = None
        # 7: count, char = -1, b -> res = dbdcdab -> no push -> prev = None




    