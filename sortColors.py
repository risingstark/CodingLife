# Sort Colors

# Given an array nums with n objects colored red, white, or blue, 
# sort them in-place so that objects of the same color are adjacent, 
# with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
 
# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 
# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

class Solution(object):
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # time: O(n^2), space(1)
        colors = [0,1,2]
        ord_i = 0
        i = 0
        while i < len(nums):
            if nums[i] != colors[ord_i]:
                j = i+1
                while j < len(nums) and nums[j] != colors[ord_i]:
                    j+=1
                # no same color left to sort
                if j == len(nums):
                    ord_i +=1
                    i-=1
                else:
                    nums[i],nums[j] = nums[j],nums[i]
            i+=1
        return nums


    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # time: O(n), space(1)
        # Loop invariant: entries in nums[:i] are all 0, and entries in nums[k+1:] are all 2.
        i = 0
        k = len(nums)-1
        j = i
        while j <= k:
            if i < j and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1


if __name__ =="__main__":
    s = Solution()
    nums = [2,0,2,1,1,0]
    print(s.sortColors2(nums))
    