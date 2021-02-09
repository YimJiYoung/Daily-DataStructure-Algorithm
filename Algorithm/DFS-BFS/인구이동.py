# 인구 이동
# https://www.acmicpc.net/problem/16234

from collections import deque
import sys

input = sys.stdin.readline


def move_population(y, x):  # (y, x) 시작 점으로 bfs로 탐색하면서 연합 찾고 인구 업데이트
    queue = deque([(y, x)])
    union = [(y, x)]
    union_population = board[y][x]

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[ny][nx]:
                continue
            if L <= abs(board[ny][nx] - board[y][x]) <= R:
                queue.append((ny, nx))
                union.append((ny, nx))
                union_population += board[ny][nx]
                visited[ny][nx] = True

    if len(union) > 1:  # 연합을 이루는 국가 1개 이상일 경우 - 인구 이동
        avg = union_population // len(union)
        for y, x in union:
            board[y][x] = avg
        return True

    return False


N, L, R = map(int, input().split(' '))
board = [[] for _ in range(N)]
total_count = 0

for i in range(N):
    board[i] = list(map(int, input().split(' ')))

while True:  # 인구 이동 없을 때까지 반복
    count = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                moved = move_population(i, j)
                if moved:
                    count += 1
    if count == 0:
        break
    total_count += 1

print(total_count)
