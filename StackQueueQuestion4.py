from collections import deque
def solution(prices):
    '''(list) -> list
    return number of period in seconds that the price goes last given list, prices contain stock prices. 
    '''
        
    queue = deque(prices)
    answer = []

    while queue:
        pop_value = queue.popleft()
        if len(queue) > 0:
            for i in range(len(queue)):
                if pop_value > queue[i] or i == len(queue)-1:
                    answer.append(i+1)
                    break
        
    answer.append(0)

    return answer


if __name__ == "__main__":

    prices = [1, 2, 3, 2, 3]
    print("answer should be = [4, 3, 1, 1, 0]", solution(prices))