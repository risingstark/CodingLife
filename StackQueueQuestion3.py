from collections import deque

def solution(arrangement):
    ''' (string) -> int
    return a number of sticks that are cutted by lazers. The given arrangement contains lazers and sticks.
    The '()' indicates lazser. 
    The '(' indicates open stick and ')' indicates close stick
    Sticks are always closed and arrangment < 100,000
    '''
    queue = deque(arrangement.replace("()","L"))
    stack = []
    lazer = []
    count = 0
    answer = 0

    while queue:
        pop_value = queue.popleft()
        # either lazser or stick
        if pop_value == '(':
            stack.append(1)
            lazer.append(0)
        elif pop_value == ')':
            answer += lazer.pop() + 1
        # pop value is lazer
        else:
            count += 1
            while queue[0] == 'L':
                queue.popleft()
                count += 1
            for i in range(len(lazer)):
                lazer[i] = lazer[i] + count
            count = 0
    return answer


if __name__ == "__main__":

    arrangement = "()(((()())(())()))(())"
    print("answer should be 17 = ",solution(arrangement))