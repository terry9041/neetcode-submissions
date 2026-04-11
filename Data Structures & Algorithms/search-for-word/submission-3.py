class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r,c,i):
            if i == len(word):
                return True
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == word[i]:
                temp = board[r][c]
                board[r][c] = "#"

                if dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1):
                    return True
                
                board[r][c] = temp
            
            return False


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
            
        return False