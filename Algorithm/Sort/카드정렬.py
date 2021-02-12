# 카드 정렬하기
# https://www.acmicpc.net/problem/1715

# 두 묶음씩 고르고 합치면서 하나의 묶음으로 만들 때 최소 비교 횟수 구하기
# key : 가장 작은 두 묶음을 합치기 -> min heap 사용

import heapq
import sys

input = sys.stdin.readline

n = int(input())

bundles = []
count = 0

for _ in range(n):
    bundle = int(input())
    heapq.heappush(bundles, bundle)

while bundles:
    if len(bundles) < 2:
        print(count)
        break

    bundle1 = heapq.heappop(bundles)
    bundle2 = heapq.heappop(bundles)

    count += bundle1 + bundle2
    heapq.heappush(bundles, bundle1 + bundle2)
