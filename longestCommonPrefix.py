# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 1:
            return strs[0]
        if not strs:
            return ""
    
        comp_val = strs[0]
        pref = ""
        j = len(comp_val)
        
        for i,word in enumerate(strs[1:]):
            
            while 0 < j:
                if comp_val[:j] == word[:j]:
                    pref = comp_val[:j]
                    j = len(pref)
                    break
                else:
                    j-=1
            if j == 0:
                return ""
        return pref
            
if __name__=="__main__":
    s = Solution()
    strs = ["flower","flow","flight"]

    print("fl" == s.longestCommonPrefix(strs))

