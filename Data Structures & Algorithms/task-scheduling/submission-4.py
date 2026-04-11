import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task]  = counts.get(task, 0) + 1
        maxHeap = [-counts[task] for task in counts]
        heapq.heapify(maxHeap)
        
        queue = deque()
        time = 0

        while maxHeap or queue:
            time += 1
            if maxHeap:
                new_count = heapq.heappop(maxHeap) + 1
                if new_count != 0:
                    queue.append((new_count, time+n))
            if queue and queue[0][1] <= time:
                count, _ = queue.popleft()
                heapq.heappush(maxHeap, count)
            
        return time