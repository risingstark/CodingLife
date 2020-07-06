import heapq
from collections import deque

def solution(operations):
    """(list) -> (list)
    given list, operations is consisted of strings that has letter space and number in order.
    "I Number" indicate insert Number, "D 1" indicate delete maximum value. "D -1", 
    indicate delete minumum value. return [0,0] if list is an empty after executing all operations.
    otherwise return [maximum, minumum].
    
    note: 
    1 < len(operations) < 1000000
    ignore delete operation with an empty list
    """
    answer = []
    heap = []
    for operation in operations:
        sign, number = operation.split(" ")
        if sign == "I":
            heapq.heappush(heap,int(number))
        elif sign == "D" and len(heap)>0:
            if number == "-1":
                heapq.heappop(heap)
            else:
                heap.pop(-1)
    if len(heap) > 0:
        answer = deque(sorted(heap))
        return [answer[-1],answer[0]]
    else:
        return [0,0]

    return answer

if __name__ == "__main__":

    operations = ["I 16","D 1"]
    print("solution should be [0,0]",solution(operations))
    operations1 = ["I 7","I 5","I -5","D -1"]
    print("solution1 should be [7,5]",solution(operations1))
    operations2 = ["I 7"]
    print("solution1 should be [7,7]",solution(operations2))