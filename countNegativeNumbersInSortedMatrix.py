# Count Negative Numbers in a Sorted Matrix

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

# Example 1:
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

# Example 2:
# Input: grid = [[3,2],[1,0]]
# Output: 0
 
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
 
# time: O(n + m), space: O(1), where n is the number of rows and m is the number columns in a given grid
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        row, col = len(grid)-1, 0
        cnt = 0
        while row >= 0 and col < len(grid[0]):
            if grid[row][col] < 0:
                cnt += len(grid[row])-col
                row-=1
            else:
                col+=1
        return cnt
            
    