from collections import deque
def solution(prices):
    '''(list) -> list
    return number of period in seconds that the price goes last given list, prices contain stock prices. 
    '''

    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer



if __name__ == "__main__":

    prices = [1, 2, 3, 2, 3]
    print("answer should be = [4, 3, 1, 1, 0]", solution(prices))