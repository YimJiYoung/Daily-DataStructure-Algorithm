# 경쟁적 전염
# https://www.acmicpc.net/problem/18405

from collections import deque

n, k = map(int, input().split(' '))
board = [[] for _ in range(n)]
viruses = []

for i in range(n):
    board[i] = list(map(int, input().split(' ')))
    for j in range(n):
        if board[i][j] != 0:
            viruses.append((board[i][j], i, j))

target_s, target_x, target_y = map(int, input().split(' '))

viruses.sort()
q = deque(viruses)
s = 0

# bfs 사용 - 1초마다 상하좌우로 증식
while q:
    if s == target_s:
        break
    size = len(q)
    for _ in range(size):
        virus, x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            # 범위 멋어나는 경우 or 0이 아님
            if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] != 0:
                continue
            board[nx][ny] = virus
            q.append((virus, nx, ny))
    s += 1

print(board[target_x - 1][target_y - 1])
