# Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # time : O(log(n+m))
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = (m + n - 1) // 2
        lo, hi = 0, m
        while lo < hi:
            i = (lo + hi) // 2
            if after-i-1 < 0 or a[i] >= b[after-i-1]:
                hi = i
            else:
                lo = i + 1
        i = lo
        nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
        first = nextfew[0]
        last = nextfew[1 - (m+n)%2]
        return (first + last) / 2.0
    
if __name__ == "__main__":
    s = Solution()
    # num1 = [1,4,5]
    # num2 = [2,3]
    # print(s.findMedianSortedArrays(num1,num2))
    
    num1 = [2,3,6,8]
    num2 = [1,4,5,7,9]
    print(s.findMedianSortedArrays(num1,num2))
    