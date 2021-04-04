# 어른 상어
# https://www.acmicpc.net/problem/19237


import copy

# 주어진 방향에 다음 위치 계산


def get_pos(cur_pos, direction_num):
    direction = directions[direction_num]
    next_pos = [cur_pos[0] + direction[0], cur_pos[1] + direction[1]]
    return next_pos


# 상어 위치 옮기기
def move_shark(shark_num, shark_pos, direction, priority):
    moved = False
    y, x = shark_pos
    possible_pos = []
    # 우선 순위 방향 순으로 이동
    for next_direction in priority:
        ny, nx = get_pos(shark_pos, next_direction)
        # 범위 밖
        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            continue
        # 자신이 있던 칸 이동 가능한 칸 배열에 추가
        if board[ny][nx][0] == shark_num:
            possible_pos.append((ny, nx, next_direction))
        # 냄새가 있는 칸 -> 이동할 수 없음
        if board[ny][nx][0] != 0:
            continue
        # 자기보다 작은 번호의 상어를 만나 격자 밖으로 쫓겨남
        if new_board[ny][nx][0] != 0 and new_board[ny][nx][0] < shark_num:
            return None

        # 이후 냄새가 업데이트될 것을 고려하여 k + 1로 설정
        new_board[ny][nx] = (shark_num, k + 1)
        shark_directions[shark_num - 1] = next_direction
        moved = True
        return (ny, nx)
    # 이동할 수 있는 칸 없으면 자기의 냄새가 있는 칸으로 이동
    if not moved:
        ny, nx, next_direction = possible_pos[0]
        new_board[ny][nx] = (shark_num, k + 1)
        shark_directions[shark_num - 1] = next_direction
        return (ny, nx)


# board의 냄새 정보 업데이트
def update_smell():
    for i in range(n):
        for j in range(n):
            if board[i][j][1] > 0:
                board[i][j] = (board[i][j][0], board[i][j][1] - 1)
            if board[i][j][1] == 0:
                board[i][j] = (0, 0)


n, m, k = map(int, input().split(' '))
board = []
directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
shark_pos = [None] * m
shark_directions = []
shark_priorities = []

shark_num = m

# 보드 초기화 - (상어 번호, 냄새 사라지기까지의 시간)
for i in range(n):
    row = list(map(int, input().split(' ')))
    board.append(row)
    for j in range(n):
        if board[i][j] != 0:
            shark_pos[board[i][j] - 1] = (i, j)
            board[i][j] = (board[i][j], k)
        else:
            board[i][j] = (board[i][j], 0)

shark_directions = list(map(int, input().split(' ')))

for _ in range(m):
    priority = []
    for _ in range(4):
        priority.append(list(map(int, input().split(' '))))
    shark_priorities.append(priority)

count = 0
# 1번 상어만 남게될 떄까지
while shark_num > 1:
    new_board = copy.deepcopy(board)

    for i in range(m):
        if not shark_pos[i]:
            continue
        next_pos = move_shark(
            i + 1, shark_pos[i], shark_directions[i], shark_priorities[i][shark_directions[i] - 1])
        if not next_pos:
            shark_num -= 1
            shark_pos[i] = None
        else:
            shark_pos[i] = next_pos

    board = new_board
    update_smell()

    count += 1
    if count >= 1000:
        break

if shark_num == 1:
    print(count)
else:
    print(-1)
