from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        directions = [(-1,0), (1,0),(0,-1), (0,1)]
        
        while queue:
            r,c = queue.popleft()
            for dr, dc in directions:
                tr, tc = dr+r, dc+c
                if 0 <= tr < rows and 0 <= tc < cols and grid[tr][tc] == 2147483647:
                    grid[tr][tc] = grid[r][c] + 1
                    queue.append((tr,tc))
        
        return