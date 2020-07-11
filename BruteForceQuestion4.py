def solution(brown, yellow):
    '''(int, int) -> list
    return a list contains length and width of carpet given the number of brown and yellow grids.
    '''

    total_n = brown + yellow
    answer = []
    for i in range(3,total_n//2):
        if (total_n%i) == 0 and (total_n//i)*2+(i-2)*2 == brown and total_n//i >= i:
            answer = [total_n//i,i]
    return answer

if __name__ == "__main__":

    brown = 24
    yellow = 24
    print(solution(brown,yellow))