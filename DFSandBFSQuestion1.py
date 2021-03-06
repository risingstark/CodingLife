def dfs(array, numbers, target, size):
    '''(int, list, int, int) -> int
    help function using DFS algorithm.
    '''
    answer = 0 
    if len(array) == size: 
        if sum(array) == target: 
            return 1
        else: 
            return 0
    else:
        A = numbers.pop(0)
        for i in [1, -1]:
            array.append(A * i)
            answer += dfs(array, numbers, target, size)
            array.pop()
        numbers.append(A)
        return answer 

def solution(numbers, target):
    '''(list, int) -> int
    return the possible number produced given the combinations of sum, minus, divide, multiple of numbers.
    '''
    answer = 0
    answer += dfs([numbers[0]], numbers[1:], target, len(numbers))
    answer += dfs([-numbers[0]], numbers[1:], target, len(numbers))
    return answer

if __name__ == "__main__":

    numbers = [1, 2, 3]
    target = 0
    print(solution(numbers,target))