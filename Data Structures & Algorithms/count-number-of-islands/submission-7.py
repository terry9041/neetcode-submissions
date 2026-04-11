class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # return 0 if grid is None
        if not grid:
            return 0

        islands = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r,c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":

                # sink island if we have seen it
                grid[r][c] = "0"

                # explore right, down, left, top
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r + 1, c)
                dfs(r, c - 1)
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)

        return islands