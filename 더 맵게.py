from heapq import heapify, heappush,heappop
def solution(scoville, K):
    heapify(scoville)
    count = 0
    while scoville[0] < K :
        count += 1
        smallest = heappop(scoville)
        if len(scoville) == 0:
            return -1
        second_Smallest = heappop(scoville)
        heappush(scoville, smallest + (2 * second_Smallest))
    return count