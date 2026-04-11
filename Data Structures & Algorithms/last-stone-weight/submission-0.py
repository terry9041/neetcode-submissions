class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        # TC: O(NlogN)
        # SC: O(1) due to inplace maxHeap

        # O(N) for heapify
        # note that heapq is minHeap by default, * -1 for maxHeap
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)


        while (len(stones) > 1):
            x = heapq.heappop(stones) * -1
            y = heapq.heappop(stones) * -1
            diff = abs(x-y) * -1 # rmb to *-1 before heappush
            if diff != 0:
                heapq.heappush(stones, diff)

        if stones:
            return stones[0] * -1
        return 0

        # # TC: O(n*n) due to naiive insert approach
        # # SC: O(1)

        # stones.sort()
        # while len(stones) > 1:
        #     x = stones.pop(-1)
        #     y = stones.pop(-1)
        #     diff = abs(x-y)
        #     if diff != 0:
        #         inserted = False
        #         for i in range(len(stones)):
        #             if stones[i]>diff:
        #                 stones.insert(i, diff)
        #                 inserted = True
        #                 break
        #         if not inserted: # wt if no elem is bigger than it, then it is biggest
        #             stones.append(diff) # insert max at the back
        # if stones:
        #     return stones[0]
        # return 0
        