from collections import deque
def solution(bridge_length, weight, truck_weights):
    num_of_truck = len(truck_weights)
    queue = deque(truck_weights)
    truck_passed = []
    time = 0
    bridge_queue = deque([0]*bridge_length)
    bridge_totalweight = 0
    while (len(truck_passed) != num_of_truck):
        time += 1
        if ( len(queue) != 0  and  bridge_totalweight - bridge_queue[0] + queue[0] <= weight):
            bridge_totalweight += queue[0]
            bridge_queue.append(queue.popleft())
            if (bridge_queue[0] !=0 ):
                bridge_totalweight -= bridge_queue[0]
                truck_passed.append(bridge_queue.popleft())
            else:
                bridge_queue.popleft()
        else:
            bridge_queue.append(0)
            if (bridge_queue[0] != 0):
                bridge_totalweight -= bridge_queue[0]
                truck_passed.append(bridge_queue.popleft())
            else:
                bridge_queue.popleft()
    return time










