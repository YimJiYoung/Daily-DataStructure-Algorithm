from itertools import combinations


def can_observe_student(x, y, board):
    n = len(board)
    tx = x
    ty = y

    while tx < n:
        if board[y][tx] == 'S':
            return True
        if board[y][tx] == 'O':
            break
        tx += 1

    tx = x
    while tx >= 0:
        if board[y][tx] == 'S':
            return True
        if board[y][tx] == 'O':
            break
        tx -= 1

    while ty < n:
        if board[ty][x] == 'S':
            return True
        if board[ty][x] == 'O':
            break
        ty += 1

    ty = y
    while ty >= 0:
        if board[ty][x] == 'S':
            return True
        if board[ty][x] == 'O':
            break
        ty -= 1

    return False


n = int(input())
board = [None]*n
empty_area = []
teacher_area = []

for i in range(n):
    board[i] = input().split(' ')
    for j in range(n):
        if board[i][j] == 'X':
            empty_area.append((j, i))
        elif board[i][j] == 'T':
            teacher_area.append((j, i))

for obstacle_area in combinations(empty_area, 3):
    for x, y in obstacle_area:
        board[y][x] = 'O'

    can_avoid = True

    for x, y in teacher_area:
        if can_observe_student(x, y, board):
            can_avoid = False
            break

    if can_avoid:
        print('YES')
        exit(0)

    for x, y in obstacle_area:
        board[y][x] = 'X'

print('NO')
