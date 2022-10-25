# Minimum Path Sum

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

 

# Example 1:


# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 100

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dynamic programming
        # time: O(mn), space: O(mn)
        # initialization
        m,n = len(grid),len(grid[0])
        table = [[0]*n for _ in range(m)]
        table[0][0] = grid[0][0]
        
        for i in range(1,m):
            table[i][0] = table[i-1][0] + grid[i][0]
        for j in range(1,n):
            table[0][j] = table[0][j-1] + grid[0][j]
            
        for i in range(1,m):
            for j in range(1,n):
                table[i][j] = grid[i][j] + min(table[i-1][j], table[i][j-1])
            
        return table[m-1][n-1]
