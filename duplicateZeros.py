# Duplicate Zeros
# Given a fixed-length integer array arr, duplicate each occurrence of zero, 
# shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place and do not return anything.

# Example 1:
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# Example 2:
# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]
 
# Constraints:
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 9

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        # 2 pointers of first and last index in arr
        left,right =0, len(arr)-1
        
        while left < right:
            
            if arr[left] == 0:
                arr[left+2:] = arr[left+1:right]
                arr[left+1] = 0
                left+=2
            else:
                left+=1


if __name__ == "__main__":

    s = Solution()
    arr = [1,0,2,3,0,4,5,0]
    arr2 = [0,0,0,0,0,0,0]
    print(s.duplicateZeros(arr))
    print(s.duplicateZeros(arr2))
