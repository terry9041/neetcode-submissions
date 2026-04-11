class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.minHeap, self.k  = nums, k

        # O(N) as u scan through the heap bottom-up to switch with parents
        heapq.heapify(self.minHeap)

        # O(N log N) as each pop is O(logN)
        # by removing the smallest num until size of k
        # we can ensure the min elem of heap is k-th largest
        while(len(self.minHeap)) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # O(1) check before inserting

        # if it is smaller than our current candidate, then it's impossible for it to be kth largest

        # also wt if the array size is smaller than k
        # then we need to populate the arry first, instead of rejecting the incoming elem

        if len(self.minHeap) < self.k or val > self.minHeap[0]:
            heapq.heappush(self.minHeap, val)

            # again, if the array is not populate enough
            # do not pop
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)

        # return the min elem as array[0]
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)