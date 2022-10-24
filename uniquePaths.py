# Unique Paths

# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
 

# Constraints:

# 1 <= m, n <= 100


import collections
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """        

        # dynamic programming
        # time: O(mn), space: O(mn)
        grid = [[0]*n for _ in range(m)]
        for i in range(m):
            grid[i][0] = 1
        for j in range(n):
            grid[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[m-1][n-1]
        

        
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """  
        # using BFS
        # base case
        if m == 1 and n == 1:
            return 1
        
        res = 0
        
        q = collections.deque()
        q.append((0,0))
        
        # down, right
        dy = [1,0]
        dx = [0,1]
        while q:
            y,x = q.popleft()
            
            for i in range(2):
                ny = dy[i] + y
                nx = dx[i] + x
                
                if ny == m-1 and nx == n-1:
                    res+=1
                elif ny < m and nx < n:
                    q.append((ny,nx))
        
        return res
