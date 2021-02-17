import sys

input = sys.stdin.readline

n = int(input())
plan = []
dp = [0] * (n + 1)  # 해당 일에서 남은 기간동안 받을 수 있는 최대 금액

for _ in range(n):
    t, p = map(int, input().split(' '))
    plan.append((t, p))

dp[n - 1] = plan[n - 1][1] if plan[n - 1][0] == 1 else 0

for i in reversed(range(n - 1)):  # 뒤에서부터 계산
    days, amount = plan[i]
    # 상담을 했을 경우(dp[i + days] + amount), 하지 않았을 경우(dp[i + 1])의 최대 값 계산
    if i + days <= n:
        dp[i] = max(dp[i + 1], dp[i + days] + amount)
    else:
        dp[i] = dp[i + 1]

# print(dp)
print(dp[0])
