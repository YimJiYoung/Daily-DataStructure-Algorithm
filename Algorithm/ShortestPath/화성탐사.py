import heapq

n = int(input())
space = []

for _ in range(n):
    row = list(map(int, input().split(' ')))
    space.append(row)

distances = [[float('inf')] * n for _ in range(n)]
distances[0][0] = space[0][0]
q = [(distances[0][0], 0, 0)]  # cost i j

while q:
    cost, y, x = heapq.heappop(q)

    # 이미 처리된 노드
    if distances[y][x] < cost:
        continue

    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny = dy + y
        nx = dx + x

        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            continue

        if distances[ny][nx] < cost + space[ny][nx]:
            distances[ny][nx] = cost + space[ny][nx]
            heapq.heappush(q, (distances[ny][nx], ny, nx))

print(distances[n - 1][n - 1])
