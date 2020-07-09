from itertools import permutations

def is_prime(n):

    """(int) -> bool
    return True iff given int, n is a prime. otherwise return False.
    """

    # 0 and 1 are not prime numbers
    if n < 2:
        return False
    # 2 is only an even prime number
    if n == 2:
        return True
    # all even numbers are not prime
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def solution(numbers):
    '''(string) -> int
    return the maximum number of primes that can made from numbers.
    '''
    answer = 0

    # split all numbers and add into list
    lst = ','.join(numbers).split(',')
    possible = []

    # find permutation numbers of given numbers
    for i in range(len(numbers)):
        possible.extend(list(permutations(lst, i+1)))
    
    possible = [''.join(i) for i in possible]
    # set(list) remove duplicate value in list
    possible = sorted(list(set(map(int, possible))))

    # remove 0 and 1 value from list
    idx = -1
    for i in range(len(possible)):
        if possible[i] <= 1: 
            idx = i
        else: 
            break
    if idx != -1: 
        possible = possible[idx+1:]

    for num in possible:
        if is_prime(num):
            answer += 1
    return answer

if __name__ == "__main__":

    numbers = "17"
    print("answer should be 3 = ",solution(numbers))