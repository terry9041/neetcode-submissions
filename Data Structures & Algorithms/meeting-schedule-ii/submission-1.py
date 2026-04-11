"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        import heapq
        heap = []

        # sort interval by start to make sure right processing order
        intervals.sort(key = lambda x : x.start)
        
        # start the heap with the first interval's end
        heapq.heappush(heap, (intervals[0]).end)

        for i in range(1, len(intervals)):
            curr = intervals[i]

            # if the new meeting can be done at the same time with the earliest one
            # reuse that room
            if curr.start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, curr.end)

        return len(heap)

        # TC: O(nlogn), sort => nlogn, each heappush is logn and we doing n => nlogn
        # SC: O(n) for the min heap
        
