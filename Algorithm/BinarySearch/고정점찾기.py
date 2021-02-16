# 고정점 찾기
# 고정점이란 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미한다.
# 하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 오름차순으로 정렬되어 있다.
# 이 수열에서 고정점이 있다면, 고정점을 출력하는 프로그램을 작성하세요. (최대 1개 존재, 없으면 -1)
# log(N)

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))


def get_fixed_point(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < mid:  # value < index -> 왼쪽 부분(값이 인덱스 값보다 작음) 탐색할 필요 없음
            start = mid + 1
        elif arr[mid] > mid:  # value > index -> 오른쪽 부분(값이 인덱스 값보다 큼) 탐색할 필요 없음
            end = mid - 1
        else:  # value == index
            return arr[mid]
    return -1


print(get_fixed_point(arr))
