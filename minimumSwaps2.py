def minimumSwaps(arr):
    
    # time : O(n), space: O(n)
    # use dictionary to keep track of value and index

    swap = 0
    arr_dict ={}

    for i,v in enumerate(arr):
        arr_dict[v] = i

    for i,v in enumerate(arr):
        if arr[i] != i+1:
            swap +=1
            arr[i] = i+1
            # swap
            arr[arr_dict[i+1]] = v
            arr_dict[v] = arr_dict[i+1]
    
    return swap
                                    

if __name__ == '__main__':

    arr = [4,3,1,2]
    print(minimumSwaps(arr))
