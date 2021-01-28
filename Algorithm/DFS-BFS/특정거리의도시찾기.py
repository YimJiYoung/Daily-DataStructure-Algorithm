import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split(' '))

answer = []
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)

queue = deque([x])
visited[x] = True
dist = 0

while queue:
    size = len(queue)
    if dist > k:  # 거리가 k보다 커지면
        break
    for _ in range(size):
        node = queue.popleft()

        if dist == k:  # 거리가 k이면
            answer.append(node)

        for neighbor in graph[node]:  # 연결된 노드 추가
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    dist += 1

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for node in answer:
        print(node)
