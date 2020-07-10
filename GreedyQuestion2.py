def solution(number, k):
    '''(string, int) -> string
    return the maximum number of combinations in order from the given string, 
    number except k out of total number
    ex. 
    number = '1924', k = 2
    answer = 94

    number = '1231234', k = 3
    answer = '3234'
    '''
    
    stack = [number[0]]
    for num in number[1:]:
        while k > 0 and stack[-1] < num and len(stack) > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
    
if __name__ == "__main__":

    number = '1924'
    k = 2
    print("answer = 94", solution(number,k))