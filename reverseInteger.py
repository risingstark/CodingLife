# Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
# then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
 
# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Constraints:
# -231 <= x <= 231 - 1

from turtle import numinput


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        res = 0
        neg = False
        
        if x < 0:
            neg = True    
            x = x * (-1)

        while x > 0:
            num = x % (10)
            res = res*(10) + num
            x = x // (10)
        
        if -2**(31) >= res or res >= 2**(31) -1:
            return 0
        
        if neg:
            return -(res)
        return res

if __name__ == "__main__":

    s = Solution()
    x = -123
    print(s.reverse(x))
