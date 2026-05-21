class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                if("row", row, value) in seen:
                    return False
                if("col",col,value) in seen:
                    return False
                if("box",row//3,col//3,value) in seen:
                    return False
                seen.add(("row",row,value))
                seen.add(("col",col,value))
                seen.add(("box",row//3,col//3,value))
        return True


       
        