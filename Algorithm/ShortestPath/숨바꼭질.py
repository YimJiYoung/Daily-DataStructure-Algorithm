# 숨바꼭질
# 1번 헛간에서 최단 거리가 가장 먼 헛간 구하기
# 거리가 1이므로 BFS로 풀 수도 있음

import heapq

n, m = map(int, input().split(' '))

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split(' '))
    # 양방향
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


# 다익스트라
distances = [float('inf')] * n  # 첫번째 노드에서 각 노드까지의 최단 거리
distances[0] = 0

q = [(0, 0)]  # 거리, 노드

while q:
    dist, node = heapq.heappop(q)  # 최단 거리 짧은 순으로

    if dist > distances[node]:
        continue

    for neighbor in graph[node]:
        if distances[neighbor] > distances[node] + 1:  # 거리가 더 짧아질 때 - 갱신
            distances[neighbor] = distances[node] + 1
            heapq.heappush(q, (distances[neighbor], neighbor))

max_node = 0
max_distance = 0
result = []

for i in range(n):
    if max_distance < distances[i]:
        max_node = i
        max_distance = distances[i]
        result = [max_node]
    elif max_distance == distances[i]:
        result.append(i)

print(max_node + 1, max_distance, len(result))

# 플로이드

# for k in range(n):
#     for a in range(n):
#         for b in range(a + 1, n):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#             graph[b][a] = graph[a][b]

# for row in graph:
#     print(row)
