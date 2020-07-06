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


if __name__ == "__main__":

    #jobs = [[0,1],[1,2],[500,6]]
    #jobs = [[0, 3], [1, 9], [2, 6]]
    jobs = [[0,2], [3,2], [6,]]
    print(solution(jobs))