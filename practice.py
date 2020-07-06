import heapq
from collections import deque

def solution1(jobs):
    tasks = deque(sorted([(x[0], x[1]) for x in jobs], key=lambda x: (x[0], x[1])))
    print("0,1",deque(sorted([(x[0], x[1]) for x in jobs])))
    print("0,1,1,0",deque(sorted([(x[0], x[1]) for x in jobs], key=lambda x: (x[1], x[0]))))
    print("1,0",deque(sorted([(x[1], x[0]) for x in jobs])))
    print("1,0,1,0",deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0]))))
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

def test(array):
    
    task = deque(sorted(array))
    return task

if __name__ == "__main__":

    #jobs = [[0,1],[1,2],[500,6]]
    #jobs = [[0, 3], [1, 9], [2, 6]]
    jobs = [[10,1], [10,2], [10,3],[1,2], [1,3],[1,4]]
    #print(solution1(jobs))
    solution1(jobs)
    #array = [5,1,2,3,4]
    #print(test)