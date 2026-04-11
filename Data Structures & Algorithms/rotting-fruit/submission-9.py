from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        queue = deque()


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        if fresh_count == 0:
            return 0
        
        minutes = 0

        def valid_range(r,c):
            return 0 <= r < rows and 0 <= c < cols

        while queue and fresh_count > 0:
            minutes += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                r, c = curr[0], curr[1]
                if valid_range(r-1,c) and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    queue.append((r-1,c))
                    fresh_count -= 1
                if valid_range(r+1,c) and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    queue.append((r+1,c))
                    fresh_count -= 1
                if valid_range(r,c-1) and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    queue.append((r,c-1))
                    fresh_count -= 1
                if valid_range(r,c +1) and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    queue.append((r,c+1))
                    fresh_count -= 1

        return minutes if fresh_count == 0 else -1
                
                

