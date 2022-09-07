# Graph Question

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
# take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, 
# return any of them. If it is impossible to finish all courses, return an empty array.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0.
# So the correct course order is [0,1].

# Example 2:
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. 
# To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# Example 3:
# Input: numCourses = 1, prerequisites = []
# Output: [0]
 
# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.

# ==================================================================================
# write code here
# ==================================================================================
import collections

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        # directed graph, G contains nodes of numCourses. 
        # G(dictionary, key= prerequisite, items = set() of courses)
        # Color list(0,1,2), 0 = not visited, 1 = visiting, 2= done visiting
        # DFS return False if there is a cycle or ...

        def dfs(i):
            
            color[i] = 1
            if i in graph:
                for j in graph[i]:
                    # graph has a cycle
                    if color[j] == 1:
                        return False
                    # j is not visited, check j's prerequisites
                    elif color[j] == 0:
                        if not dfs(j):
                            return False
            res.appendleft(i)
            color[i] = 2
            return True     
            
        # initialize queue
        res = collections.deque([])
        # create directed graph
        graph = {}
        for c,p in prerequisites:
            if p not in graph:
                graph[p] = set([c])
            else:
                graph[p].add(c)
                
        color = [0]*numCourses
        for i in range(numCourses):
            # node i not visited
            if color[i] == 0:
                if not dfs(i):
                    return []
        return list(res)
        
        
        



if __name__ == "__main__":

    s = Solution()
    numCourses = [2,4,1]
    prerequisites= [[[1,0]],[[1,0],[2,0],[3,1],[3,2]],[]]
    output = [[0,1],[0,2,1,3],[0]]
    for i in range(len(numCourses)):
            print(s.findOrder(numCourses[i],prerequisites[i])==output[i])

