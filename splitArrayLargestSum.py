# Split Array Largest Sum

# Given an array nums which consists of non-negative integers and an integer m, 
# you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.
 
# Example 1:
# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.

# Example 2:
# Input: nums = [1,2,3,4,5], m = 2
# Output: 9

# Example 3:
# Input: nums = [1,4,4], m = 3
# Output: 4 

# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 106
# 1 <= m <= min(50, nums.length)

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        
        # binary search
        # time : O(), space: O()
        
        left,right = max(nums), sum(nums)
        
        while left < right:
            mid = (left+right)//2
            sm = 0
            count = 1
            for num in nums:
                if sm+num > mid:
                    count+=1
                    sm=num
                else:
                    sm+=num
                
            if count > m:
                left = mid +1
            else:
                right = mid
        return right
    
    
        # lo, hi = max(nums), sum(nums)
        # while lo < hi:
        #     mid = (lo+hi)//2
        #     tot, cnt = 0, 1
        #     for num in nums:
        #         if tot+num<=mid: 
        #             tot += num
        #         else:
        #             tot = num
        #             cnt += 1
        #     if cnt>m: lo = mid+1
        #     else: hi = mid
        # return hi