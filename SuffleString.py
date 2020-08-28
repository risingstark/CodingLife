from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        new_s = list(s)
        print(new_s)
        for i in range(len(new_s)):
            new_s[i] = s[indices[i]]
            print(new_s[i])
        final_s = ''.join(new_s)
        return final_s


if __name__ == "__main__":

    s = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    a = Solution()
    print(a.restoreString(s, indices))
