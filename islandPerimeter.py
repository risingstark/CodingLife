# # Island Perimeter

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). 
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.

# Example 1:
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

# Example 2:
# Input: grid = [[1]]
# Output: 4

# Example 3:
# Input: grid = [[1,0]]
# Output: 4
 
# Constraints:
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # directions: up, down, left, right
        dy = [-1,1,0,0]
        dx = [0,0,-1,1]
        res = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                # check island
                if grid[row][col] == 1:
                    
                    # check up, down, left, right
                    for i in range(4):
                        check_row = dy[i] + row
                        check_col = dx[i] + col
                        
                        # check boundray
                        if check_row < 0 or check_row >= len(grid) or check_col < 0 or len(grid[0]) <= check_col:
                            res+=1
                        # check water
                        elif grid[check_row][check_col] == 0:
                            res+=1
        return res

if __name__ == "__main__":

    s = Solution()
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(s.islandPerimeter(grid))