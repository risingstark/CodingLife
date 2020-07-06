import heapq
from collections import deque

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
    for i in range(total_ele+1):
        while jobs and jobs[0][0] <= start:
            (req,time) = heapq.heappop(jobs)
            heapq.heappush(heap,(time,req))
        if len(heap) > 0:
            (time, req) = heapq.heappop(heap)
            answer += time + max(0, start-req)
            start = time + max(start, req)
        elif len(jobs) > 0: 
            if jobs[0][0] > start:
                start = jobs[0][0]


    return int(answer/total_ele)

def solution1(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)



if __name__ == "__main__":

    #jobs = [[0,1],[1,2],[500,6]]
    #jobs = [[0, 3], [1, 9], [2, 6]]
    jobs = [[0,2], [3,2], [6,2]]
    print(solution(jobs))