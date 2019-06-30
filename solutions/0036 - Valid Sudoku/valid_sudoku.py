class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isNine(row):
            already = []
            for num in row:
                if num != ".":
                    if num in already:
                        return False
                    else:
                        already.append(num)
            return True

        for i in range(9):
            if not isNine(board[i]):
                return False
            if not isNine([row[i] for row in board]):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not isNine([board[0 + i][0 + j], board[0 + i][1 + j], board[0 + i][2 + j], board[1 + i][0 + j],
                              board[1 + i][1 + j], board[1 + i][2 + j], board[2 + i][0 + j], board[2 + i][1 + j],
                              board[2 + i][2 + j]]):
                    return False
        return True
            
