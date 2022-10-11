# Word Search

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

# Constraints:
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        # up, down, left, right
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        
        stack = []
        
        # board check left to right, up to bottom
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0]:
                    check = set()
                    stack.append((y,x,0,False))
                    
                    # DFS
                    while stack:
                        ny,nx,pos,backtrack = stack.pop()
                        
                        if backtrack:
                            check.remove((ny,nx))
                            continue
                        check.add((ny,nx))
                        stack.append((ny,nx,pos,True))
                        if board[ny][nx] == word[pos]:                        
                            if pos == len(word)-1:
                                return True

                            for i in range(4):
                                yi = ny + dy[i]
                                xi = nx + dx[i]
                                if  (yi,xi) in check:
                                    continue
                                if 0 <= yi < len(board) and 0 <= xi < len(board[0]) and pos+1 < len(word) and (yi,xi) not in check:
                                    stack.append((yi,xi,pos+1,False))
        
        return False                    
                    
if __name__ == "__main__":
    s = Solution()
    board = [["A","A"]]
    word = "A"
    print(s.exist(board,word))