import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.cap = k
        while len(self.heap) > self.cap:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.cap:
            heapq.heappop(self.heap)
        return self.heap[0]

    # assume m adds -> TC: O(mlogk) where log k is for inserting and popping one elem in size k heap
    # SC: O(k) for the size of the heap


