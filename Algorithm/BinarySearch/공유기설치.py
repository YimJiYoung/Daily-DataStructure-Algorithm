# 공유기 설치
# https://www.acmicpc.net/problem/2110

# 파라메트릭 서치 유형
# 최적화 문제를 결정 문제로 바꾸어 해결
# 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제 -> 범위 내에서 조건을 만족하는 가장 큰(작은) 값 이진 탐색으로 범위를 좁하갈 수 있다.

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, c = map(int, input().split(' '))
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

# 인접한 공유기 사이의 거리에 대해 이진 탐색
start = 1
end = arr[n - 1] - arr[0]
gap = 1

while start <= end:
    mid = (start + end) // 2
    count = 1
    prev = 0  # 이전에 공유기 설치된 index

    for i in range(1, n):  # 현재 mid를 gap으로 했을 때 설치 가능한 공유기 수 계산
        if arr[i] >= arr[prev] + mid:
            count += 1
            prev = i

    if count >= c:  # 거리 증가시키기
        start = mid + 1
        gap = mid
    else:  # 거리 감소시키기
        end = mid - 1

print(gap)
