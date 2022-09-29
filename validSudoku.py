# # 36. Valid Sudoku

# Determine if a 9 x 9 Sudoku board is valid. 
# Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 
# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
import collections

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        sub_boxes = [set(),set(),set()]
        
        for y in range(9):
            # row check
            count_row = collections.Counter(board[y])
            for k in count_row:
                if count_row[k] > 1 and k != '.':
                    return False
            
            # column check
            column_check = []
            sub_ind = 0
            for row in range(9):
                if board[row][y] != ".":
                    if board[row][y] not in column_check:
                        column_check.append(board[row][y])
                        if board[row][y] not in sub_boxes[sub_ind]:
                            sub_boxes[sub_ind].add(board[row][y])
                        else:
                            return False
                    else:
                        return False
                if (row+1) % 3 == 0:
                    sub_ind+=1
            print(column_check)
            
            # 3x3 sub-boxes initialize
            if (y+1) % 3 == 0:
                sub_boxes = [set(),set(),set()]        
        return True

if __name__ == "__main__":

    s = Solution()
    # expected False
    board1 = [
        [".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]
        ]
    # print(s.isValidSudoku(board1))

    # expected False
    board2 = [
        ["7",".",".",".","4",".",".",".","."],
        [".",".",".","8","6","5",".",".","."],
        [".","1",".","2",".",".",".",".","."],
        [".",".",".",".",".","9",".",".","."],
        [".",".",".",".","5",".","5",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]
        ]
    print(s.isValidSudoku(board2))
