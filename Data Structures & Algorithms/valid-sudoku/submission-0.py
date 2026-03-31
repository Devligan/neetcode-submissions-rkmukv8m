class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            curr = set()
            for e in row:
                if(e != '.' and e in curr):
                    return False
                curr.add(e)
        
        for column in range(len(board[0])):
            curr = set()
            for row in range(len(board)):
                if(board[row][column] != '.' and board[row][column] in curr):
                    return False
                curr.add(board[row][column])
        for r in range(3):
            for c in range(3):
                curr = set()
                for rowMove in range(3):
                    for colMove in range(3):
                        if(board[r * 3 + rowMove][c * 3 + colMove] != '.' and board[r * 3 + rowMove][c * 3 + colMove] in curr):
                            return False
                        curr.add(board[r * 3 + rowMove][c * 3 + colMove])
        return True