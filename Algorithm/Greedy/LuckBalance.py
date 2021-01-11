# Luck Balance
# https://www.hackerrank.com/challenges/luck-balance/problem


import heapq

# Complete the luckBalance function below.


def luckBalance(k, contests):
    minHeap = []
    totalLuck = 0

    for contest in contests:
        if contest[1] == 0:  # 안 중요한 경기 lose
            totalLuck += contest[0]
            continue
        heapq.heappush(minHeap, contest[0])  # 중요한 경기 minHeap에 추가

    winCount = len(minHeap) - k  # 이겨야 하는 경기 수

    while winCount > 0:
        # 가장 luck이 작은 경기부터 win
        totalLuck -= heapq.heappop(minHeap)
        winCount -= 1

    while minHeap:
        # 나머지 경기 lose
        totalLuck += heapq.heappop(minHeap)

    return totalLuck
