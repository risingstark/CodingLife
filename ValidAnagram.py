# Given two strings s1 and s2, checn if they are anagrams. 
# Two strings ar anagrams if they are made of the same characters 
# with the same frequencies

class Solution:

    # solution 1. 
    # frequency1 = frequency2    
    def validAnagram1(self,s1,s2):
        ''' (self, string, string)
        return True if given s1 and s2 are anagrams, 
        otherwise return False
        '''
        if len(s1) != len(s2):
            return False

        freq1 = self.helpBuildFreq(s1,{})
        freq2 = self.helpBuildFreq(s1,{})

        return freq1==freq2

    def helpBuildFreq(self,word,fdict):
        for s in word:
            if s not in fdict:
                fdict[s]=1
            else:
                fdict[s]+=1
        return fdict

if __name__ == "__main__":

    s1 = "danger"
    s2 = "garden"
    s = Solution()
    print(s.validAnagram1(s1,s2))

    s1 = "nameless"
    s2 = "salesman"