# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
# This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.


# example 1
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# example 2
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

# time: O(log(m)*long(n)), space: O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        left_m,right_m = 0, len(matrix)-1
        while left_m <= right_m:
            mid_m = (left_m + right_m)/2
            left_n,right_n = 0, len(matrix[mid_m])-1
            if target < matrix[mid_m][left_n]:
                right_m = mid_m-1
            elif target > matrix[mid_m][right_n]:
                left_m = mid_m+1
            else:
                while left_n <= right_n:
                    mid_n = (left_n + right_n)/2
                    if matrix[mid_m][mid_n] == target:
                        return True
                    elif matrix[mid_m][mid_n] < target:
                        left_n = mid_n+1
                    else:
                        right_n = mid_n-1
                return False
        return False


