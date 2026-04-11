class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        groups = 0

        def dfs(i,j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i,j) not in visited and grid[i][j] == "1":
                visited.add((i,j))
                print(i,j)
                dfs(i , j + 1)
                dfs(i - 1 , j)
                dfs(i , j - 1)
                dfs(i + 1, j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visited or grid[i][j] == "0":
                    pass
                else:
                    groups += 1
                    dfs(i,j)
        
        return groups


                
                
