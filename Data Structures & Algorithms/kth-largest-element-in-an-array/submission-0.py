class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # BF: sort and return 
        # TC: O(nlogn) SC: O(1)

        # Optimized: use a heap, keep max length of k
        # each insert is O(logk), n inserts -> O(nlogk)

        import heapq

        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            if i >= k:
                heapq.heappop(heap)
            
        return heap[0]
