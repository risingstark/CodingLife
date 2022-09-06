# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0
        d = {}
        j = 0
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                j = max(j, d[s[i]]+1)
                d[s[i]] = i
            res = max(res, i-j+1)
        return res


if __name__ == "__main__":
    
    s = "abba"
    t = Solution()
    print(t.lengthOfLongestSubstring(s))

