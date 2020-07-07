from collections import deque
def solution(priorities, location):
    '''(list, int) -> int
    given the priorities is a list contains priorities of requested prints. 
    The location is an int, indicates where the requested print is.
    return a number when the requested print in location comes out in order.
    '''

    p_print = deque(priorities)
    answer = 1
    done = False
    while not done:
        max_value = max(p_print)
        if location == 0 and max_value == p_print[0]:
            done = True
        else:
            pop_value = p_print.popleft()
            if location == 0:
                if max_value > pop_value:
                    p_print.append(pop_value)
                    location = len(p_print)-1
            # location != 0
            else:
                if location != 0 and max_value <= pop_value:
                    answer+=1
                    location -= 1
                elif location !=0 and max_value > pop_value:
                    p_print.append(pop_value)
                    location -=1
    return answer


if __name__ == "__main__":

    priorities = [2, 1, 3, 2]
    location = 2
    #priorities = [1, 1, 9, 1, 1, 1]
    #location = 0
    print("answer shuold 5 == ", solution(priorities, location))