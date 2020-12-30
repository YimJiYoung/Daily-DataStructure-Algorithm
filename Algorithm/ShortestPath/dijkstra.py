import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 노드에서 b 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for node, cost in graph[start]:
        distance[node] = cost
    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for node, cost in graph[now]:
            distance[node] = min(distance[node], distance[now] + cost)


dijkstra(start)

print(distance)
