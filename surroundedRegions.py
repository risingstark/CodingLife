# Surrounded Regions

# Given an m x n matrix board containing 'X' and 'O', 
# capture all regions that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example 1:
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.

# Example 2:
# Input: board = [["X"]]
# Output: [["X"]]

# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        # Phase 1: "Save" every O-region touching the border, changing its cells to 'S'.
        # Phase 2: Change every 'S' on the board to 'O' and everything else to 'X'.

        if not any(board): return

        m, n = len(board), len(board[0])
        edge_cordinates = []
        
        for k in range(max(m, n)):
            edges = (0, k), (m-1, k), (k, 0), (k, n-1)
            for edge in (edges):
                if edge not in edge_cordinates and edge[0] < m and edge[1] < n:
                    edge_cordinates.append(edge)
                

        while edge_cordinates:
            i, j = edge_cordinates.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = "S"
                edge_cordinates += (i, j-1), (i, j+1), (i-1, j), (i+1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "S":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        return board


if __name__ == "__main__":
    s = Solution()
    board1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print(s.solve(board1))
    board2 = [["O","O","O"],["O","O","O"],["O","O","O"]]
    print(s.solve(board2))
