# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이떄 이 수열에서 x가 등장하는 횟수를 계산하세요.
# 시간 복잡도 O(logN)으로 알고리즘 설계하지 않으면 '시간 초과' 판정

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, x = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

# left_index = bisect_left(arr, x)
# right_index = bisect_right(arr, x)

# count = right_index - left_index
# print(right_index, left_index)

# if count <= 0:
#     print(-1)
# else:
#     print(count)


def first(arr, x):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        elif arr[mid] >= x:
            end = mid - 1
        else:
            start = mid + 1
    return None


def last(arr, x):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if (mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return None


def count_by_range(arr, x):
    a = first(arr, x)

    if a == None:
        return 0

    b = last(arr, x)

    return b - a + 1


count = count_by_range(arr, x)

if count <= 0:
    print(-1)
else:
    print(count)
