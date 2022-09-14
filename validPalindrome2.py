# Valid Palindrome II
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:

# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false

# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.
class Solution(object):

    # time: O(n), space: O(1)
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def palindrom_check(left,right):
            
            while left <= right:
                print(left, right)
                if s[left] == s[right]:
                    left+=1
                    right-=1
                else:
                    return False
            return True
        
        # 2 pointers of start and last index of s
        left, right = 0, len(s)-1    
        while left <= right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                if palindrom_check(left+1,right) or palindrom_check(left,right-1):
                    return True
                else:
                    return False
        return True


if __name__ == "__main__":

    s = Solution()
    t = "ABCA"
    print(s.validPalindrome(t))