from collections import deque


def solution(block):
    n = len(block)
    m = len(block[0])
    queue = deque([(0, 0)])
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    step = 0

    while queue:
        step += 1
        length = len(queue)
        for _ in range(length):
            y, x = queue.popleft()
            if y == n-1 and x == m-1:  # 끝에 도달
                return step
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_y = y + dy
                next_x = x + dx
                if next_y >= n or next_y < 0 or next_x >= m or next_x < 0:
                    continue
                if block[next_y][next_x] == 1 and not visited[next_y][next_x]:
                    queue.append((next_y, next_x))
                    visited[next_y][next_x] = True
    return step


print(solution([
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]))
