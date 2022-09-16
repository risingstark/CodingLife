# Backspace String Compare

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
# '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.


# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
 
# Constraints:
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
 
# Follow up: Can you solve it in O(n) time and O(1) space?
import itertools

class Solution(object):
    # time: O(n), space: O(n)
    def backspaceCompare1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def build_string(bstr):
            
            res = []
            for c in bstr:
                if c == "#":
                    if len(res) > 0:
                        res.pop()
                else:
                    res.append(c)
            return res
        
        return build_string(s) == build_string(t)
        
    # time : O(n), space: O(1)
    def backspaceCompare2(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def F(S):
            skip = 0
            for char in reversed(S):
                if char == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield char
        return all(x == y for x, y in itertools.izip_longest(F(S),F(T)))

    
if __name__ == "__main__":
    a = Solution()
    s = "ab#c"
    t = "ad#c"
    print(a.backspaceCompare1(s,t))
