# Container With Most Water

# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, 
# such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

 

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #time: O(n^2), space: O(1)
        # n = len(height)
        # max_val = 0
        # for i in range(0, n-1):
        #     for j in range(i+1,n):
        #         temp_val = (j-i) * min(height[i],height[j])
        #         if max_val < temp_val:
        #             max_val = temp_val
        # return max_val
        
        # time: O(n), space(1)        
        i,j = 0, len(height)-1
        max_val = 0
        while i < j:
            temp_val = (j-i) * min(height[i],height[j])
            if max_val < temp_val:
                max_val = temp_val
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        return max_val
            