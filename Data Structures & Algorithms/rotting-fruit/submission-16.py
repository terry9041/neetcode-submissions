from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        queue = deque()

        # 1. set up by counting fresh and add rot to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        # if no fresh, then time required is 0
        if fresh_count == 0:
            return 0

        directions = [(0,1), (0, -1), (1,0), (-1,0)]
        time = 0

        # 2. process the rot by multisource bfs
        while fresh_count > 0 and queue:
            time += 1
            lvl_size = len(queue)
            for _ in range(lvl_size):
                r,c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr,nc))

        # 3. check if all fresh are rot eventually
        if fresh_count > 0:
            return -1
        
        return time
