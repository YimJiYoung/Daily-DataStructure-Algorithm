from collections import deque
import copy


def get_next_pos(cur_pos, direction):
    diff = [(-1, 0), (-1, -1), (0, -1), (1, -1),
            (1, 0), (1, 1), (0, 1), (-1, 1)]
    next_pos = (cur_pos[0] + diff[direction - 1][0],
                cur_pos[1] + diff[direction - 1][1])
    return next_pos


def get_fish_pos(board, fish):
    for x in range(4):
        for y in range(4):
            if board[x][y][0] == fish:
                return (x, y)


def get_shark_pos(board):
    for x in range(4):
        for y in range(4):
            if board[x][y][0] == -1:
                return (x, y)


def move_all_fish(board, gone_fish):
    fish = 1
    # 물고기 이동
    while fish <= 16:
        pos = get_fish_pos(board, fish)
        while fish in gone_fish:
            fish += 1
            pos = get_fish_pos(board, fish)
        if not pos:
            return
        x, y = pos

        if board[x][y][0] == shark:  # 상어
            continue
        direction = board[x][y][1]
        nx, ny = get_next_pos((x, y), direction)
        # 이동할 수 없는 경우
        while nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or board[nx][ny][0] == shark:
            direction = (direction + 1) % 8
            nx, ny = get_next_pos((x, y), direction)
        # 위치 교체
        board[x][y], board[nx][ny] = board[nx][ny], (board[x][y][0], direction)

        fish += 1


def get_next_shark_pos(board, shark_pos):  # 다음으로 가능한 상어의 위치 반환
    next_pos = []
    x, y = shark_pos
    direction = board[x][y][1]

    diff = [(-1, 0), (-1, -1), (0, -1), (1, -1),
            (1, 0), (1, 1), (0, 1), (-1, 1)]

    while True:
        nx, ny = (x + diff[direction - 1][0], y + diff[direction - 1][1])
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            break
        if board[nx][ny][0] != 0:
            next_pos.append((nx, ny))
        x, y = nx, ny

    return next_pos


board = []

for _ in range(4):
    fish_info = list(map(int, input().split(' ')))
    row = []
    for i in range(0, len(fish_info), 2):
        row.append((fish_info[i], fish_info[i + 1]))
    board.append(row)

shark = -1
gone_fish = [board[0][0][0]]
board[0][0] = (shark, board[0][0][1])  # 상어
answer = 0

q = deque([(board, gone_fish)])

while q:
    board, gone_fish = q.popleft()

    if len(gone_fish) == 16:
        continue

    move_all_fish(board, gone_fish)
    shark_pos = get_shark_pos(board)
    possible_pos = get_next_shark_pos(board, shark_pos)
    # print(possible_pos)

    for next_pos in possible_pos:
        new_board = copy.deepcopy(board)
        new_gone_fish = gone_fish[:]
        new_gone_fish.append(board[next_pos[0]][next_pos[1]][0])
        new_board[next_pos[0]][next_pos[1]] = (
            shark, new_board[next_pos[0]][next_pos[1]][1])
        new_board[shark_pos[0]][shark_pos[1]] = (0, 0)
        q.append((new_board, new_gone_fish))
        answer = max(answer, sum(new_gone_fish))

print(answer)
