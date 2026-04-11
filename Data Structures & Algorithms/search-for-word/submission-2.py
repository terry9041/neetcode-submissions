class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r,c):
            if len(path) == len(word):
                print(path)
                return True
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == word[len(path)] and (r,c) not in path:
                path.add((r,c))
                if dfs(r+1,c) or dfs(r-1,c) or dfs(r,c-1) or dfs(r,c+1):
                    return True
                path.remove((r,c))
            else:
                return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c):
                    return True
        
        return False