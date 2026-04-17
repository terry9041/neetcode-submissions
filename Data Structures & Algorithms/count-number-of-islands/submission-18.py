from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Can we modify the input grid in-place? No
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = set()

        def bfs(r,c):
            visited.add((r,c)) # mark as visited
            queue = deque()
            queue.append((r,c))
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    tr, tc = dr+row, dc+col
                    if 0 <= tr < rows and 0 <= tc < cols and (tr,tc) not in visited and grid[tr][tc] == "1":
                        visited.add((tr,tc)) # mark as visited
                        queue.append((tr,tc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited: 
                    islands += 1
                    bfs(r,c)
        
        return islands

        # TC: O(m*n)
        # SC: O(min(m,n))
        
                