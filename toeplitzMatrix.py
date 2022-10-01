# Toeplitz Matrix
# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.


# Example 1:
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.

# Example 2:
# Input: matrix = [[1,2],[2,2]]
# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.
 
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 20
# 0 <= matrix[i][j] <= 99

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        # time: O(m+n), space: O(1)
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if y+1 < len(matrix) and x+1 < len(matrix[0]):
                    if matrix[y][x] != matrix[y+1][x+1]:
                        return False
        return True