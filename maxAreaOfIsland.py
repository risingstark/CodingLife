# Max Area of Island

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.


# Example 1:
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# Example 2:
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # up, down, left, right
        nx = [0,0,-1,1]
        ny = [1,-1,0,0]
        
        global_max = 0
        stack = []
        
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                
                if grid[j][i] == 1:
                    local_max = 0
                    stack.append((j,i))
                    
                    while stack:
                        y,x = stack.pop()
                        if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == 1:
                            grid[y][x] = 2
                            local_max +=1
                            for k in range(0,4):
                                dx = nx[k] + x
                                dy = ny[k] + y
                                
                                stack.append((dy,dx))
                    if local_max > global_max:
                        global_max = local_max
        return global_max
                    
                    

if __name__ == "__main__":

    s = Solution()
    grid = [[1]]
    print(s.maxAreaOfIsland(grid))