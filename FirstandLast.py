# given a storted array of integers arr and integer target,
# find the index of the first and last position of target in arr.
# in target can't be found in arr, return [-1. -1]
# input = [2,4,5,5,5,5,5,7,9,9]
# target = 5
# output = [2,6]

class Solution:
    
    # soluotion 1
    # using for loop, time: O(N), space: O(1)
    def first_and_last1(self,arr,target):
        
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
    # using binary search to find firt and last occurance of target in arr
    # time: O(logN), space: O(1)
    def first_and_last2(self,arr,target):

        if len(arr) == 0 or arr[-1] < target or arr[0] > target:
            return [-1,-1]
        first = self.find_start(arr,target)
        end = self.find_end(arr,target)
        return [first,end]

    def find_start(self,arr,target):
        
        if len(arr) == 0:
            return 0
        left, right = 0, len(arr)-1
        while left<=right:
            mid = (left+right)//2
            if arr[mid] == target and arr[mid-1] < target:
                return mid
            elif arr[mid] < target:
                left = mid +1
            else:
                right = mid-1
        return -1

    def find_end(self,arr,target):

        if arr[-1] == target:
            return len(arr)-1
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid]==target and arr[mid+1] > target:
                return mid
            elif arr[mid] > target:
                left = mid+1
            else:
                right = mid-1
        return -1            

        
if __name__=="__main__":

    arr = [2,4,5,5,5,5,5]
    target = 5
    output = [2,6]
    s = Solution()
    print(s.first_and_last1(arr,target) == output)
    print(s.first_and_last2(arr,target) == output)