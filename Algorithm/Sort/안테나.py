import sys
from functools import reduce

input = sys.stdin.readline

n = int(input())
homes = list(map(int, input().split(' ')))
# 중앙값일 때 합의 최소가 된다 (극단적인 값에 영향 받지 않음)
homes.sort()
print(homes[(n - 1) // 2])

# if length % 2 == 1:
#     print(homes[length // 2])
# else:
#     mid1_sum = reduce(lambda acc, cur: acc + abs(cur -
#                                                  homes[length // 2]), homes, 0)
#     mid2_sum = reduce(lambda acc, cur: acc + abs(cur -
#                                                  homes[length // 2 - 1]), homes, 0)
#     if mid1_sum < mid2_sum:
#         print(homes[length // 2])
#     else:
#         print(homes[length // 2 - 1])
