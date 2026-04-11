import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task]  = counts.get(task, 0) + 1
        maxHeap = [(-counts[task], task) for task in counts]
        heapq.heapify(maxHeap)
        
        queue = deque()
        time = 0

        while maxHeap or queue:
            print(maxHeap, queue)
            if maxHeap:
                count, task = heapq.heappop(maxHeap)
                if count != -1:
                    queue.append((count+1, task, time+n))
            if queue and queue[0][2] <= time:
                count,task, _ = queue.popleft()
                heapq.heappush(maxHeap, (count,task))
            time += 1
        return time