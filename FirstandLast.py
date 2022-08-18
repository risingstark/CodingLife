# given a storted array of integers arr and integer target,
# find the index of the first and last position of target in arr.
# in target can't be found in arr, return [-1. -1]
# input = [2,4,5,5,5,5,5,7,9,9]
# target = 5
# output = [2,6]

class Solution:
    
    # soluotion 1
    # using for loop, time: O(N), space: O(1)
    def firstandlast1(self,arr,target):
        
        res = []
        for i,v in enumerate(arr):
            if v == target and len(res)==0:
                res.append(i)
                while i <= len(arr)-1 and arr[i] == target:
                    i+=1
                res.append(i-1)
                return res
        return [-1,-1]
        


    # solution 2
    # using binary search
    def firstandlast2(self,arr,target):

        res = []


        return res

if __name__=="__main__":

    arr = [2,4,5,5,5,5,5]
    target = 5
    output = [2,6]
    s = Solution()
    print(s.firstandlast1(arr,target) == output)
