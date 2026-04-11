from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        
        
        rows, cols = len(grid), len(grid[0])

        visited = set()
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))

        time = -1

        def valid_range(r,c):
            return 0 <= r < rows and 0 <= c < cols

        while queue:
            lvl_size = len(queue)
            time += 1
            for _ in range(lvl_size):
                curr = queue.popleft()
                r, c = curr[0], curr[1]
                if valid_range(r-1,c) and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    queue.append((r-1,c))
                if valid_range(r+1,c) and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    queue.append((r+1,c))
                if valid_range(r,c-1) and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    queue.append((r,c-1))
                if valid_range(r,c +1) and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    queue.append((r,c+1))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        if time == -1:
            return 0
            
        return time
                
                

