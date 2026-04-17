from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    tr, tc = dr+row, dc+col
                    if 0 <= tr < rows and 0 <= tc < cols and grid[tr][tc] == "1":
                        grid[tr][tc] = "0"
                        queue.append((tr,tc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    islands += 1
                    bfs(r,c)
        
        return islands
                