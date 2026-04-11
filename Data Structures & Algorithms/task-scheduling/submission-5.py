import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # TC: O(m) SC: O(k)
        counts = {}
        for task in tasks:
            counts[task]  = counts.get(task, 0) + 1

        # TC: O(k) SC: O(k)
        maxHeap = [-counts[task] for task in counts]
        heapq.heapify(maxHeap)
        
        queue = deque()
        time = 0
 
        # TC: O(total_time * logk)
        while maxHeap or queue:
            time += 1
            # TC: O(logk)
            if maxHeap:
                new_count = heapq.heappop(maxHeap) + 1
                if new_count != 0:
                    queue.append((new_count, time+n))
            # TC: O(logk)
            if queue and queue[0][1] <= time:
                count, _ = queue.popleft()
                heapq.heappush(maxHeap, count)
            
        return time

        # total_time >= m, k is constant

