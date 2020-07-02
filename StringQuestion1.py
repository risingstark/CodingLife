import string

def solution(s, n):
    ''' (string, int) -> string
    given string s is consisted of upper, lower and blank. 
    Convert each letter in s to next nth letter in alphabet.
    return -1 in case of an empty list
    ex.
    solution("AB",4) -> "EF"
    '''
    alphabet_low = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase

    if len(s) < 1:
        return -1    
    for i in range(len(s)):
        if s[i] in alphabet_low:
            if alphabet_low.index(s[i]) + n > 25:
                new_ind = alphabet_low.index(s[i]) + n - 25
            else:
                new_ind = alphabet_low.index(s[i]) + n
            s = s.replace(s[i],alphabet_low[new_ind])
        elif s[i] in alphabet_upper:
            if alphabet_upper.index(s[i]) + n > 25:
                new_ind = alphabet_upper.index(s[i]) + n - 25
            else:
                new_ind = alphabet_upper.index(s[i]) + n
            s = s.replace(s[i],alphabet_upper[new_ind])

    return s

if __name__ == "__main__":

    s = "AB"
    n = 4
    print(solution(s,n))
