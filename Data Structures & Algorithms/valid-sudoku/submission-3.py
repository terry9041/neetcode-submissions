class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                curr = board[r][c]

                if curr == ".":
                    continue

                if ("row", r, curr) in seen or ("col", c, curr) in seen or ("box", r//3 * 3 + c//3, curr) in seen:
                    return False

                seen.add(("row", r, curr))
                seen.add(("col", c, curr))
                seen.add(("box", r//3 * 3 + c//3, curr))

        return True
                
            

        

        
                