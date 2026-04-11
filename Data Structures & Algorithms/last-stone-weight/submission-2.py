import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
    # BF: TC O(n^2), SC O(1) asO(n) for finding max, we need to find the max pair for O(n) times
    # Optimized: use a heap to store all weights, pop 2 and insert 1 for n times
    # TC O(nlogn) SC O(n)
    # caveat is we have to store stone in * -1 as the heap in py is minheap 

        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone1, stone2 = heapq.heappop(heap), heapq.heappop(heap)
            heapq.heappush(heap, -abs(stone1-stone2))
        
        return -heap[0]