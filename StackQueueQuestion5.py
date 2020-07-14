from collections import deque

def solution(s):

    s = deque(s.replace('()',''))
    stack = []

    for i in s:
        if i == '(':
            stack.append('(')
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False

if __name__ == "__main__":

    s = "(())()"
    print(solution(s))