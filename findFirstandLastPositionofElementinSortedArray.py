# # Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
 
# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # time: O(logn), space: O(1)
        def search_for(nums, target, left=True):
            
            l, r = 0, len(nums)

            while l < r:
                mid = (l+r)//2
                if nums[mid] == target:
                    if left:
                        r = mid
                    else:
                        l = mid + 1
                elif nums[mid] < target:
                    l = mid +1
                else:
                    r = mid
            return l

        start = search_for(nums,target,True)
        last = search_for(nums,target,False)

        if len(nums) < 1:
            return [-1,-1]
        elif 0 <= start < len(nums) and nums[start] == target:
            return [start,last-1]
        else:
            return [-1,-1]

        
if __name__ == "__main__":

    s = Solution()
    nums = [1,2,3,4,5,5,5,6,7]
    target = 5
    print(s.searchRange(nums,target))