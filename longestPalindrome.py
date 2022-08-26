# You are given an array of strings words. Each element of words 
# consists of two lowercase English letters.
# Create the longest possible palindrome by selecting some elements 
# from words and concatenating them in any order. 
# Each element can be selected at most once.
# Return the length of the longest palindrome that you can create. 
# If it is impossible to create any palindrome, return 0.
# A palindrome is a string that reads the same forward and backward.

# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
# Note that "clgglc" is another longest palindrome that can be created.

# Input: words = ["ab","ty","yt","lc","cl","ab"]
# Output: 8
# Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
# Note that "lcyttycl" is another longest palindrome that can be created.

# Input: words = ["cc","ll","xx"]
# Output: 2
# Explanation: One longest palindrome is "cc", of length 2.
# Note that "ll" is another longest palindrome that can be created, and so is "xx".

# 1 <= words.length <= 105
# words[i].length == 2
# words[i] consists of lowercase English letters.

import collections

class Solutions:
    def longestPalindrome(self,words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        count = collections.Counter(words)
        flag_odd = False
        res = 0

        for k,v in count.items():
            # case1
            rev_k = k[::-1]
            if k == rev_k:
                if v % 2 ==1:
                    if not flag_odd:
                        res += v*2
                        flag_odd = True
                    else:
                        res += (v-1)*2
                else:
                    res += v*2
            # case 2
            else:
                if count[k] >0 and count[rev_k] and count[rev_k] > 0:
                    least = min(count[rev_k],v)
                    res += 4*least
                    count[k] -= least
                    count[rev_k] -= least
        return res


if __name__ == "__main__":
    s = Solutions()
    words1 = ["lc","cl","gg"]
    words2 = ["ab","ty","yt","lc","cl","ab"]
    words3 = ["cc","ll","xx"]
    print(s.longestPalindrome(words1)==6)
    print(s.longestPalindrome(words2)==8)    
    print(s.longestPalindrome(words3)==2)





