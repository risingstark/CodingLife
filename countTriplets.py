from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0
    
    for v in arr:
        if v in r3:
            count += r3[v]
        
        if v in r2:
            r3[v*r] += r2[v]
        
        r2[v*r] += 1

    return count

if __name__=="__main__":

    arr = [1,2,2,4]
    r = 2
    print(countTriplets(arr,r))