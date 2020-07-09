def help_adjust_length(p, l):
    '''(list, int) -> (list)
    help function to adjust a length of given list p to l.
    '''

    p_len = len(p)
    if p_len >= l:
        return p[:l]
    else:
        q = l // p_len
        r = len(l) - len(p_len)*q
    
    return(p*q + p[:r])

def solution(answers):
    '''(list) -> (list)
    return a person who corrects the answer most among p1,p2 and p3. Given list, answers contains less than
    10000 questions. 
    p1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...]
    '''
    answer = []
    total_len = len(answers)
    p1 = help_adjust_length([1, 2, 3, 4, 5], total_len) 
    p2 = help_adjust_length([2, 1, 2, 3, 2, 4, 2, 5], total_len) 
    p3 = help_adjust_length([3, 3, 1, 1, 2, 2, 4, 4, 5, 5], total_len)
    
    p1_count, p2_count, p3_count = 0, 0, 0

    for i in range(len(answers)):
        if p1[i] == answers[i]:
            p1_count += 1
        if p2[i] == answers[i]:
            p2_count += 1
        if p3[i] == answers[i]:
            p3_count += 1

    most = max(p1_count, p2_count, p3_count)
    if most == p1_count:
        answer.append(1)
    if most == p2_count:
        answer.append(2)
    if most == p3_count:
        answer.append(3)
    
    return answer


if __name__ == "__main__":

    #answers = [1,2,3,4,5]
    #print("answer is [1] =", solution(answers))
    answers = [1,3,2,4,2]
    print("answer is [1,2,3] =", solution(answers))