class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c,i):
            print(r,c)
            if i == len(word):
                return True
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == word[i]:
                temp = board[r][c]
                board[r][c] = "#"
                
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if dfs(nr,nc,i+1):
                        return True
                
                board[r][c] = temp
          
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        
        return False

        # dfs(0,2,0)
        #     dfs(1,2,1)
        #         dfs(1,3,2)
        #             dfs()


        