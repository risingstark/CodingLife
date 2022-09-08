# You are given a string s. We want to partition the string into as many parts as possible 
# so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, 
# the resultant string should be s.

# Return a list of integers representing the size of these parts.


# Example 1:
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

# Example 2:
# Input: s = "eccbbbbdec"
# Output: [10]
 
# Constraints:
# 1 <= s.length <= 500
# s consists of lowercase English letters.

import collections

class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        count_s = collections.Counter(s)
        res = []
        s_set = set()
        nums = 0
        
        for c in s:
            count_s[c]-=1
            nums+=1
            if c not in s_set:
                s_set.add(c)
            if count_s[c] == 0:
                s_set.remove(c)
            if len(s_set) == 0:
                res.append(nums)
                nums = 0
        return res            
                
                