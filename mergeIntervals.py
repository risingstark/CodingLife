# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
# Constraints:
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if len(intervals) ==1:
            return intervals
        intervals.sort()
        START, END = 0, 1
        prev = intervals[0]
        new_intervals = intervals[1:]
        
        merged = []
        for i,interval in enumerate(new_intervals):
            
            if prev[END] < interval[START]:
                merged += [prev]
                prev = interval
            else:
                s = min(prev[START],interval[START])
                e = max(prev[END],interval[END])
                prev = [s,e]
            
            if i == len(new_intervals)-1:
                merged+=[prev]

        return merged
    
    