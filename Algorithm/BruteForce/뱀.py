n = int(input())
k = int(input())

board = [[False]*n for _ in range(n)]

for _ in range(k):
    i, j = input().split(' ')
    board[int(i)-1][int(j)-1] = True

l = int(input())

turns = []

for _ in range(l):
    time, direction = input().split(' ')
    turns.append((int(time), direction))


time = 0
snake = [(0, 0)]  # 뱀 위치
y, x = snake[0]  # 현재 탐색 위치
direction = 0  # 동, 남, 서, 북

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def getNextPos(y, x, direction):
    return (y + dy[direction], x + dx[direction])


def getNextDir(direction, turn):
    if turn == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


while True:
    time += 1
    # 새로운 위치
    y, x = getNextPos(y, x, direction)
    # 벽에 부딪히는 경우
    if x < 0 or y < 0 or x >= n or y >= n:
        break
    # 자기 몸에 부딪히는 경우
    if (y, x) in snake:
        break
    # 사과 있는 경우 -> 꼬리 늘리기
    if board[y][x]:
        board[y][x] = False
        snake.append((y, x))
    # 사과 없는 경우 -> 꼬리 이동
    else:
        snake.append((y, x))
        snake.pop(0)
    # turn해야 하는 겅우 방향 전환
    for turn in turns:
        if time == turn[0]:
            direction = getNextDir(direction, turn[1])
    #print(time, snake)

print(time)
