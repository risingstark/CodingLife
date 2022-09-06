###### Rotting Oranges ######

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
import collections

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n,m = len(grid), len(grid[0])
        q = collections.deque()
        total_fresh_num = 0

        for y in range(n):
            for x in range(m):
                # count fresh orange
                if grid[y][x] == 1:
                    total_fresh_num +=1                
                elif grid[y][x] == 2:
                    q.append((y,x,0))                    

        seen = set()

        # up, down, left, right
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]

        while q:
            y,x,mins = q.popleft()
            for i in range(4):
                ny = dy[i] + y
                nx = dx[i] + x
                if 0 <= nx < m and 0 <= ny < n and (ny,nx) not in seen and grid[ny][nx] == 1:
                    seen.add((ny,nx))
                    total_fresh_num-=1
                    if total_fresh_num == 0:
                        return mins+1
                    q.append((ny,nx,mins+1))
    
        return 0 if total_fresh_num == 0 else -1


if __name__ == "__main__":

    s = Solution()
    # example 1
    grid1 = [[2,1,1],[1,1,0],[0,1,1]]
    print(s.orangesRotting(grid1), s.orangesRotting(grid1)==4)

    # example 2
    grid2 = [[2,1,1],[0,1,1],[1,0,1]]
    print(s.orangesRotting(grid2), s.orangesRotting(grid2)==-1)

    # example 3
    grid3 = [[0,2]]
    print(s.orangesRotting(grid3),s.orangesRotting(grid3)==0)