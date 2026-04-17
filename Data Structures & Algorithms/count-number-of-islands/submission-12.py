class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BF: second grid of same size, call it vistied
        # we could scan its neighours
        # extra space: O(m*n)

        # Changes are allowed on grid
        # what if we mark "visited" directly on grid
        # if land -> sink it to 0 as visited
        # we could save that extra space

        rows, cols = len(grid), len(grid[0])
        islands = 0

        
        def dfs(r,c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                # sink that land to mark as visited
                grid[r][c] = "0" 

                # check neighours
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r,c-1)
                dfs(r,c+1)
            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)
        
        return islands

        # TC: O(r*c) always as we check every elem in grid constant number of times
        # SC: O(r*c) due to recusion depth, worst if entire grid is just one island
