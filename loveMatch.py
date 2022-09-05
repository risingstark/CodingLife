import sys
import collections

def love(W,L):

# W = love
# L = ovle, elve, love, ove, 
    res = 0
    count_w = collections.Counter(W)

    for word in L:
        count_word = collections.Counter(word)

        count_c = 0
        for c in count_w:
            if c in count_word:
                count_word[c] >= count_w[c]
                count_c+=1
        if count_c == len(count_w):
            res+=1

    return res


if __name__ == "__main__":

    # W = input()
    # L = str(input().split(" "))
    W = "love"
    L = ["ovle", "elve", "love", "ove","looove"] 
    print(love(W,L))


