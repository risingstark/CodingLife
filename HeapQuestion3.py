import heapq

def solution(jobs):
    '''(list) -> int
    return the minimum average time given 2d array, 
    Jobs where its elements are (required time to start, tiem to take).
    '''

    heapq.heapify(jobs)
    start = jobs[0][0]
    total_ele = len(jobs)
    heap = []
    answer = 0
    for i in range(total_ele):
        while jobs and jobs[0][0] <= start:
            (s,t) = heapq.heappop(jobs)
            heapq.heappush(heap,(t,s))
        if len(heap) > 0:
            (t, s) = heapq.heappop(heap)
            answer += t + max(0, start-s)
            start = t + max(start, s)
    return int(answer/total_ele)


if __name__ == "__main__":

    jobs = [[0,1],[1,2],[500,6]]
    jobs = [[0, 3], [1, 9], [2, 6]]
    print("solution should be 3 = ",solution(jobs))