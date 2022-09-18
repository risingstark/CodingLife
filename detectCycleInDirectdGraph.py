# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(size, edges):
    """
    Solution description.

    Time Complexity: ...
    Space Complexity: ...
    """
    
    def dfs(i):
        color[i] = 1
        if i in graph:
            for j in graph[i]:
                if color[j] == 0:
                    if not dfs(j):
                        return False
                elif color[j] == 1:
                    return False
        color[i] = 2
        return True
                        
    graph = {}
    for i in range(0,size,2):
        start,last = edges[i],edges[i+1]
        if last in graph:
            graph[last].add(start)
        else:
            graph[last] = set([start])			
    color = [0]*size
    for i in range(size):
        if color[i] == 0:
            if not dfs(i):
                return False
    return True
