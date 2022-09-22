# Cheapest Flights Within K Stops

# There are n cities connected by some number of flights. 
# You are given an array flights where flights[i] = [fromi, toi, pricei] 
# indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, 
# return the cheapest price from src to dst with at most k stops. 
# If there is no such route, return -1.

# Example 1:
# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

# Example 2:
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

# Example 3:
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

# Constraints:
# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 104
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst
import heapq
import collections

class Solution(object):
    def findCheapestPrice1(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        # Dijkstra's algorithm. Time complexity: O(E + V log V), space complexity: O(V + E).        
        graph = {}
        for flight in flights:
            if flight[0] in graph:
                graph[flight[0]][flight[1]] = flight[2]
            else:
                graph[flight[0]] = {flight[1]:flight[2]}

        rec = {}
        heap = [(0, -1, src)]
        heapq.heapify(heap)
        while heap:
            cost, stops, city = heapq.heappop(heap)
            if city == dst:
                return cost
            if stops == k or rec.get((city, stops), float('inf')) < cost:
                continue
            if city in graph:
                for nei, price in graph[city].items():
                    summ = cost + price
                    if rec.get((nei, stops+1), float('inf')) > summ:
                        rec[(nei, stops+1)] = summ
                        heapq.heappush(heap, (summ, stops+1, nei))
        return -1

    # Dijkstra algo, 
    # Time: O(K * ElogV), where E is the number of edges and V is the number of Nodes
    # Space: O(N + E)
    def findCheapestPrice2(self, n, flights, src, dst, k):

        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w
        pq = [(0, src, k+1)]
        vis = [0] * n
        while pq:
            w, x, temp_k = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] >= temp_k:
                continue
            vis[x] = temp_k
            for y, dw in graph[x].items():
                heapq.heappush(pq, (w+dw, y, temp_k-1))
        return -1

if __name__ == "__main__":

    s = Solution()
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    # print(s.findCheapestPrice1(n, flights, src, dst, k))
    print(s.findCheapestPrice2(n, flights, src, dst, k))