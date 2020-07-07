from collections import deque 

def solution(bridge_length, weight, truck_weights):
    """(int, int, list) -> int
    return the minimum time of crossing all trucks through bridge. Given bridge is a one way.
    It can hold up to given weight. Truck weight count iff truck is completely on the bridge.
     """
    time = 0
    wnum = 0
    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    while wnum < len(truck_weights):
        time += 1
        bridge_weight -= bridge[0]
        bridge.popleft()
        print(bridge, time)
        if bridge_weight + truck_weights[wnum] <= weight:
            bridge.append(truck_weights[wnum])
            bridge_weight += truck_weights[wnum]
            wnum += 1
        else:
            bridge.append(0)
    answer = time + bridge_length

    return answer


if __name__ == "__main__":

    bridge_length = 2
    weight = 10
    truck_weights = [7,4,5,6]
    print("answer should be 8 = ",solution(bridge_length, weight, truck_weights))