# Sort Characters By Frequency

# Given a string s, sort it in decreasing order based on the frequency of the characters. 
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

# Example 1:
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:
# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:
# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
 

# Constraints:
# 1 <= s.length <= 5 * 105
# s consists of uppercase and lowercase English letters and digits.

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # time : O(n), space: O(n)
        s_count = collections.Counter(s)
        s_ind = [0] * (len(s)+1)
        
        for i,c in enumerate(s):
            if s_ind[s_count[c]] == 0:
                s_ind[s_count[c]] = [c]
            else:
                if c not in s_ind[s_count[c]]:
                    s_ind[s_count[c]].append(c)
                
        res = []
        for i in range(len(s_ind)-1,0,-1):
            if s_ind[i] !=0:
                for val in s_ind[i]:
                    res.append(val*i)
        
        return "".join(res)
