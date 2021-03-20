# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626


import heapq


def solution(scoville, K):
    count = 0
    foods = []
    total_scoville = 0

    for food in scoville:
        heapq.heappush(foods, food)

    while foods:
        food1 = heapq.heappop(foods)
        if food1 >= K:
            return count
        if not foods:
            return -1
        food2 = heapq.heappop(foods)
        heapq.heappush(foods, food1 + food2 * 2)  # 섞은 음식 heap에 추가
        count += 1

    return count
