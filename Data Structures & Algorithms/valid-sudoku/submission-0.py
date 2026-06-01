class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            numbers_only = [char for char in board[i] if char != '.']
            if len(set(numbers_only)) != len(numbers_only):
                return False;

        for c in range(len(board[0])):
            column_arr = []
            for r in range(len(board)):
                if board[r][c] != '.':
                    column_arr.append(board[r][c])

            if len(set(column_arr)) != len(column_arr):
                return False
        
        for box_row in [0, 3, 6]:
            for box_col in [0, 3, 6]:
                array_check = []
                
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        if board[r][c] != '.':
                            array_check.append(board[r][c])
                
                if len(set(array_check)) != len(array_check):
                    return False

        return True