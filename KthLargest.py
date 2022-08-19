# given an arrary of integers arr and and integer k, find kth largest element
# 1 <= k <= |arr|
# input arr = [4,2,9,7,5,6,7,1,3]
# k = 4
# output = 6
import heapq
from multiprocessing.sharedctypes import Array

class Solution:
    # solution 1
    # sort arr and return kth index of element
    # time : O(NlogN), space: O(1) for sort() and O(N) for sorted()
    # sorted() and sort() built-in function use TimSort, which is combined of merge and select sort
    # sorted() and sort() takes O(nlogn)
    def find_kth_largest1(self,k,arr):
        arr.sort()
        return arr[-k]


    # solution 2
    # using heap, which is priority queue
    # time: O(n+klogn) building heap takes n and heapify takes klogn, space : O(n)
    def find_kth_largest2(self,k,arr):
        # build heap
        heapq.heapify(arr)
        # nlargest returns a list contains nth largest elements in DESC order
        # note heapq.nsmallest returns a list contains nth smallest elements in ASC order
        return heapq.nlargest(k,arr)[k-1]
        

if __name__ =="__main__":

    s = Solution()
    arr = [4,2,9,7,5,6,7,1,3]
    k = 4
    output = 6
    print(s.find_kth_largest1(k,arr)==6)
    print(s.find_kth_largest2(k,arr)==6)
