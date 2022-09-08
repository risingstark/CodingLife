# Given an integer array nums of length n and an integer target, 
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0


# Constraints:
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104
# Accepted
# 875,727
# Submissions
# 1,889,151


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort() # using timsort(insertion sort + merge sort) O(nlogn)
        
        curr = nums[0] + nums[1] + nums[len(nums)-1]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if abs(target - val) < abs(target-curr):
                    curr= val
                    if curr == target:
                        return curr
                elif val < target:
                    l+=1
                else:
                    r-=1
        return curr

