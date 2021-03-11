from collections import deque


# 거리가 가장 가까운 물고기 위치 반환
def get_nearest_fish(size, pos):
    q = deque([pos])
    visited = [[False] * n for _ in range(n)]
    visited[pos[0]][pos[1]] = True
    distance = 0

    while q:
        distance += 1
        length = len(q)
        eatable_fish = []  # 먹을 수 있는 물고기 리스트
        for _ in range(length):  # 같은 거리의 칸들에 대해서
            y, x = q.popleft()

            for dy, dx in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ny = dy + y
                nx = dx + x
                # 범위 벗어나거나 이미 방문한 곳인 경우
                if ny >= n or nx >= n or ny < 0 or nx < 0 or visited[ny][nx]:
                    continue
                if board[ny][nx] > size:  # 물고기의 크기가 더 큰 경우 -> 지나갈 수 없음
                    continue
                if board[ny][nx] != 0 and board[ny][nx] < size:  # 자기보다 작은 물고기 발견
                    eatable_fish.append((ny, nx))
                q.append((ny, nx))
                visited[ny][nx] = True

        if eatable_fish:
            eatable_fish.sort()  # 가장 위에 있는, 왼쪽에 있는 물고기를 구하기 위해 정렬
            y, x = eatable_fish[0]
            return (y, x, distance)


n = int(input())
board = []
cur_pos = (0, 0)
size = 2
count = 0  # 자기와 같은 수의 물고기 먹은 개수
time = 0

for i in range(n):
    line = list(map(int, input().split(' ')))
    board.append(line)
    for j in range(n):
        if line[j] == 9:  # 아기 상어 위치
            cur_pos = (i, j)
            board[i][j] = 0

while(True):
    near_fish = get_nearest_fish(size, cur_pos)

    if not near_fish:
        break
    ny, nx, distance = near_fish
    time += distance

    count += 1
    if count >= size:
        size += 1
        count = 0

    board[ny][nx] = 0
    cur_pos = (ny, nx)


print(time)
