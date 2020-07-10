from collections import deque
def solution(prices):
    '''(list) -> list
    return number of period in seconds that the price goes last given list, prices contain stock prices. 
    '''

    answer = []
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j] < prices[i]:
                break
        answer.append(j-i)

    return answer


if __name__ == "__main__":

    prices = [1, 2, 3, 2, 3]
    print("answer should be = [4, 3, 1, 1, 0]", solution(prices))