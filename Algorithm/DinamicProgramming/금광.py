# 금광
# n x m의 크기의 금광이 있습니다. 각 칸에는 특정한 크기의 금이 들어 있으며 채굴자는 첫번째 열에서부터 출발하여 금을 캐기 시작합니다.
# 맨 처음에는 첫번째 열의 어느 행에서든 출발할 수 있습니다. 이후에 m번 걸쳐서 매번 오르쪽 위, 오른쪽, 오르쪽 아래 3가지 중 하나의 위치로 이동해야 합니다.
# 결과적으로 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.

import sys

input = sys.stdin.readline


def convert(arr, n, m):
    new_arr = []
    for i in range(0, n):
        new_arr.append(arr[i*m: i*m + m])
    return new_arr


n, m = map(int, input().split(' '))
mine = list(map(int, input().split(' ')))
mine = convert(mine, n, m)
dp = [[0] * n for _ in range(m)]  # 행, 열의 위치에서 시작했을 때 채굴할 수 있는 금의 최대 크키

for i in range(n):
    dp[m - 1][i] = mine[i][m - 1]

for col in reversed(range(m - 1)):
    # print(col)
    for row in range(n):
        dp[col][row] = dp[col + 1][row]
        if row > 0:
            dp[col][row] = max(dp[col][row], dp[col + 1][row - 1])
        if row < n - 1:
            dp[col][row] = max(dp[col][row], dp[col + 1][row + 1])
        dp[col][row] += mine[row][col]
    # print(dp[col])

print(max(dp[0]))
