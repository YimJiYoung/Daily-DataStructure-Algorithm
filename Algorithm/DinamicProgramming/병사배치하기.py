# 병사 배치하기
# https://www.acmicpc.net/problem/18353
# 가장 긴 증가하는 부분 수열(Longest Increasing Subseqeunce) 이용

import sys

input = sys.stdin.readline

n = int(input())
soldiers = list(map(int, input().split(' ')))
dp = [1] * n  # dp[i] = soldeirs[i]를 마지막 원소로 갖는 내림차순 부분 배열의 최대 길이

for i in range(1, n):
    for j in range(0, i):
        if soldiers[i] < soldiers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
