from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # 1. set up fresh_count and queue, return early if no fresh fruit from the start
        queue = deque()
        fresh_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        if fresh_count == 0:
            return 0
        
        # 2. set up directions for easy looping
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        # 3. process rotten fruits using the queue
        time = 0
        while queue and fresh_count > 0:
            lvl_size = len(queue)
            for _ in range(lvl_size):
                rot = queue.popleft()
                for dr, dc in directions:
                    fr, fc = rot[0]+dr, rot[1]+dc
                    # if fresh, rot it, decrement fresh_count, add to queue
                    if 0 <= fr < rows and 0 <= fc < cols and grid[fr][fc] == 1:
                        grid[fr][fc] = 2
                        fresh_count -= 1
                        queue.append((fr,fc))
            time += 1
        print(grid)
        
        if fresh_count > 0:
            return -1
        
        return time
        



        