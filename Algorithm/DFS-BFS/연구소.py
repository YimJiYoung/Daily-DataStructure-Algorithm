from itertools import combinations
import copy


def dfs(y, x, board):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < m and ny < n and board[ny][nx] == 0:
            board[ny][nx] = 2
            dfs(ny, nx, board)


n, m = map(int, input().split(' '))
board = [[] for _ in range(n)]
blankArea = []  # 벽 새울 수 있는 위치
answer = 0

for i in range(n):
    board[i] = list(map(int, input().split(' ')))
    for j in range(m):
        if board[i][j] == 0:
            blankArea.append((i, j))

# 빈 공간에 벽 3개 세우는 모든 조합
for walls in combinations(blankArea, 3):
    newBoard = copy.deepcopy(board)
    for i, j in walls:
        newBoard[i][j] = 1  # 벽 세우기

    for i in range(n):
        for j in range(m):
            if newBoard[i][j] == 2:
                dfs(i, j, newBoard)

    count = 0

    for i in range(n):
        for j in range(m):
            if newBoard[i][j] == 0:
                count += 1
    # print(walls, count)

    answer = max(answer, count)

print(answer)
