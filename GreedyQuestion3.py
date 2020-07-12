from itertools import permutations

def solution(number, k):
    '''(string, int) -> string
    return the maximum number of combinations from the given string, number except k out of total number
    
    ex. 
    
    number = '1924', k = 2
    answer = 94

    number = '1231234', k = 3
    answer = '4332'
    '''

    numbers = ','.join(number).split(',')
    p = list(permutations(numbers,len(numbers)-k))
    p = sorted(list(set(map(int,[''.join(i) for i in p]))))
    
    return str(p[-1]) 


if __name__ == "__main__":

    number = '1924'
    k = 2
    print("answer = 94", solution(number,k))