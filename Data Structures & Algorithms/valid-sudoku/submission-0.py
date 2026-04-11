class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seenRow = set()
            seenCol = set()
            for j in range(9):
                if '1' <= board[i][j] <='9':
                    if board[i][j] not in seenRow:
                        seenRow.add(board[i][j])
                    else:
                        return False
                if '1' <= board[j][i] <= '9':
                    if board[j][i] not in seenCol:                  
                        seenCol.add(board[j][i])
                    else:
                        return False
        for i in range(0,8,3):
            for j in range(0,8,3):
                seen = set()
                for y in range(0,3):
                    for x in range(0,3):
                        if '1' <= board[i+y][j+x] <= '9':
                            if board[i+y][j+x] not in seen:
                                seen.add(board[i+y][j+x])
                            else:
                                return False
        return True


                
            
