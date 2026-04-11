class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # return None if grid is None or the row is None
        if not grid or not grid[0]:
            return None

        maxArea = 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            # add up itself and neighbours if the cell is a valid land
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = 0
                return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
            return 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c))

        return maxArea

        # TC: O(m*n) for going thro each pair of r,c, same for any case
        # SC: O(m*n) for dfs call stack, worst case is the entire grid is one island

        