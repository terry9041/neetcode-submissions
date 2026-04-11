import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap) # O(n) heap construction where n = len(nums)
        self.cap = k

        # Maintain invariant: heap size must not exceed k
        while len(self.heap) > self.cap:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.cap:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappush(self.heap,val)
            heapq.heappop(self.heap)
        return self.heap[0]

    # intuition:
    # we only keep track of the k largest values, discard the rest
    # if we add a smaller num later, it won't affect the top k list, and the smaller ones are still useless
    # if we add a larger num later, it will affect the top k list, but still the smaller ones are still ueslsees

    # assume m adds -> TC: O(mlogk) where log k is for inserting and popping one elem in size k heap
    # SC: O(k) for the size of the heap


