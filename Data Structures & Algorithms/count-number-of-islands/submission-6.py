class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # return 0 if grid is None
        if not grid:
            return 0

        islands = 0
        
        # set up len var for access
        rows, cols = len(grid), len(grid[0])

        # dfs to traverse on 1s
        def dfs(r,c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                grid[r][c] = "0"
                dfs(r, c + 1)
                dfs(r + 1, c)
                dfs(r, c - 1)
                dfs(r - 1, c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)

        return islands