import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    pq = []
    for idx, value in enumerate(food_times):
        heapq.heappush(pq, (value, idx + 1))
    previous = 0

    while (pq[0][0] - previous)*len(pq) < k:
        k -= (pq[0][0] - previous)*len(pq)
        previous = pq[0][0]
        heapq.heappop(pq)

    result = sorted(pq, key=lambda x: x[1])
    return result[k % len(pq)][1]
