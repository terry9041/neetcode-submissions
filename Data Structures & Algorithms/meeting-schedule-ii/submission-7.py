"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)
        minHeap = [intervals[0].end]
        heapq.heapify(minHeap)
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval.end)
        return len(minHeap)