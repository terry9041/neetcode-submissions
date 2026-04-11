from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                char = board[r][c]
                if (char in row[r] or char in col[c] or char in square[(r//3, c//3)]):
                    return False
                row[r].add(char)
                col[c].add(char)
                square[(r//3,c//3)].add(char)
        
        return True


                
            
