# 위상 정렬
# 방향 그래프의 모드느 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
# 시간복잡도 O(V + E)


from collections import deque

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # node a에서 b로 연결
    # b의 진입 차수 1 증가
    indegree[b] += 1


# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    # 처음 시작할 때 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐 빌 떄까지 반복
    while q:
        node = q.popleft()
        result.append(node)

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for next_node in graph[node]:
            indegree[next_node] -= 1
            # 새롭게 진입차수가 0이 되는 노드 큐에 삽입
            if indegree[next_node] == 0:
                q.append(next_node)

    for i in result:
        print(i, end=' ')


topology_sort()
