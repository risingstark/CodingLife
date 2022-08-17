# Given two strings s1 and s2, checn if they are anagrams. 
# Two strings ar anagrams if they are made of the same characters 
# with the same frequencies
class Solution:

    # solution 1. 
    # frequency1 = frequency2
    # Time complexity : O(N), Space : O(N)
    def validAnagram1(self,s1,s2):
        ''' (self, string, string)
        return True if given s1 and s2 are anagrams, 
        otherwise return False
        '''
        if len(s1) != len(s2):
            return False

        freq1 = self.helpBuildFreq(s1,{})
        freq2 = self.helpBuildFreq(s2,{})

        for key in freq1:
            if key not in freq1 or freq1[key] != freq2[key]:
                return False
        return True

    def helpBuildFreq(self,word,fdict):
        for s in word:
            if s not in fdict:
                fdict[s]=1
            else:
                fdict[s]+=1
        return fdict

    # solution2
    # using sorted(), which is built-in, using TimSort(); combine mergesort and selectionsort
    # sorted() takes O(nlogn) and space space(N)
    def validAnagram2(self,s1,s2):
        
        if len(s1) != len(s2):
            return False
        
        return sorted(s1) == sorted(s2)

if __name__ == "__main__":

    s1 = "danger"
    s2 = "garden"
    s = Solution()
    print(s.validAnagram1(s1,s2))

    s1 = "debit card"
    s2 = "bad credit"
    print(s.validAnagram2(s1,s2))
