# Custom Sort String

# You are given two strings order and s. 
# All the characters of order are unique and were sorted in some custom order previously.
# Permute the characters of s so that they match the order that order was sorted. 
# More specifically, if a character x occurs before a character y in order, 
# then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

# Example 1:
# Input: order = "cba", s = "abcd"
# Output: "cbad"
# Explanation: 
# "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
# Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

# Example 2:
# Input: order = "cbafg", s = "abcd"
# Output: "cbad"
 

# Constraints:
# 1 <= order.length <= 26
# 1 <= s.length <= 200
# order and s consist of lowercase English letters.
# All the characters of order are unique.
import collections

class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        # tiem: O(n+m), space: O(m), where n is the length of order and m is the length of s
        s_count = collections.Counter(s)
        res = ""
        for c in order:
            if c in s_count:
                res+= s_count[c]*c
                del s_count[c]
                
        for v in s_count:
            res+= s_count[v]*v
            
        return res