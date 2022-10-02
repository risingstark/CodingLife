# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution(object):

    # time: O(n^2), space: O(1)
    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = set()
        nums.sort()
        for i in range(len(nums)-2):
            left = i +1
            right = len(nums)-1
            while left < right and nums[left] < 1:
                if -nums[i] == nums[left] + nums[right]:
                    res.add((nums[i],nums[left],nums[right]))
                    left+=1
                elif -nums[i] < nums[left] + nums[right]:
                    right-=1
                else:
                    left+=1

        return list(res)


    #     res = set()
    #     nums.sort()
        
    #     for i in range(len(nums)-2):
    #         if i > 0:
    #             return list(res)
    #         l,r = i+1, len(nums)-1
    #         while l < r:
    #             val = nums[i] + nums[l] + nums[r]
    #             if val == 0:
    #                 res.add((nums[i],nums[l],nums[r]))
    #                 l+=1
    #             elif val < 0:
    #                 l+=1
    #             else:
    #                 r-=1
    #     return list(res)

    # # time: O(n^2), space: O(1)
    # # optimization version from threeSum1()
    # def threeSum2(self, nums):
    #         """
    #         :type nums: List[int]
    #         :rtype: List[List[int]]
    #         """
    #         res = []
    #         n = len(nums)
    #         nums = sorted(nums)
    #         for i in range(n-2):
    #             if i > 0 and nums[i] == nums[i-1]:
    #                 continue
    #             j = i+1
    #             k = n-1
    #             new_target = -nums[i]
    #             while j < k:
    #                 summ = nums[j] + nums[k]
    #                 if summ < new_target:
    #                     j += 1
    #                 elif summ > new_target:
    #                     k -= 1
    #                 else:
    #                     res.append([nums[i], nums[j], nums[k]])
    #                     # removing duplicate answer
    #                     while j < k and nums[j+1] == nums[j]:
    #                         j += 1
    #                     j += 1
    #                     # removing duplicate answe
    #                     while k > j and nums[k-1] == nums[k]:
    #                         k -= 1
    #                     k -= 1
    #         return res


if __name__ == "__main__":

    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    # print(s.threeSum1(nums))
    print(s.threeSum1(nums))
    # print(s.threeSum2(nums))


