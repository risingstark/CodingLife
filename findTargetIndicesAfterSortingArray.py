# Find Target Indices After Sorting Array

# You are given a 0-indexed integer array nums and a target element target.
# A target index is an index i such that nums[i] == target.
# Return a list of the target indices of nums after sorting nums in non-decreasing order. 
# If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

# Example 1:
# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.

# Example 2:
# Input: nums = [1,2,5,2,3], target = 3
# Output: [3]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.

# Example 3:
# Input: nums = [1,2,5,2,3], target = 5
# Output: [4]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 5 is 4.
 
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i], target <= 100


class Solution(object):
    def targetIndices1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # time: O(nlogn), space: O(n)
        nums.sort()        
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res

    def targetIndices2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # time: O(nlogn), space: O(n)
        nums.sort()
        def search_for(nums,target,left=True):
        
            start, last = 0, len(nums)
            
            while start < last:
                mid = (start+last)/2
                
                if nums[mid] == target:
                    if left:
                        last = mid
                    else:
                        start = mid +1
                elif nums[mid] < target:
                    start = mid +1
                else:
                    last = mid
            return start
        
        l = search_for(nums,target,True)
        r = search_for(nums,target,False)
        
        return list(range(l,r))


    def targetIndices3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # time: O(n), space: O(n)
        smaller,cnt = 0,0
        for num in nums:
            if num < target:
                smaller +=1
            elif num == target:
                cnt+=1
        
        return list(range(smaller,smaller+cnt))


if __name__ == "__main__":

    s = Solution()
    nums = [1,5,2,4,3]
    target = 3
    print(s.targetIndices3(nums,target))