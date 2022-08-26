#==================================================================================================
# Given a characters array tasks, representing the tasks a CPU needs to do, 
# where each letter represents a different task. Tasks could be done in any order.
#  Each task is done in one unit of time. For each unit of time, 
# the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period 
# between two same tasks (the same letter in the array), 
# that is that there must be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all the given tasks.

# examples
# ex1
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: 
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.

# ex2
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.

# ex3
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation: 
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
#==================================================================================================
import collections


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # our intuition is to schedule these tasks row-by-row, 
        # where each row has at least n + 1 tasks.
        # get the sorted frequences of different letters in descending order: 
        # f_1, f_2, ..., f_l, so we get l columns with heights f_1, f_2, ..., f_l.
        # find the maximal frequency 'f_max' and its repeated times 'num_f_max',
        # if num_f_max >= n + 1: 
        #   the scheduled sequence is row_1, row_2, ..., row_(f_max)
        # if num_f_max < n + 1: 
        #   there are (n + 1 - num_f_max) * (f_max - 1) empty spaces needed to be filled,
        # we can use the remaining tasks to fill them column-by-column
        # from the tasks from higher frequency to lower one, add idles if necessary.
        # The scheduled sequence is row_1, row_2, ..., row_(f_max).
        
        if tasks == []:
            return 0
        freqs = list(collections.Counter(tasks).values())
        print(freqs)
        f_max = max(freqs)
        num_f_max = freqs.count(f_max)
        
        needed_to_fill = (n + 1 - num_f_max) * (f_max - 1)
        remaining = len(tasks) - f_max * num_f_max
        
        return f_max * num_f_max + max(needed_to_fill, remaining)
    
if __name__=="__main__":

    tasks = ["A","A","A","A","B","B","B","B","C","C","D","D","E"]
    n = 3
    s = Solution()
    print(s.leastInterval(tasks,n))
