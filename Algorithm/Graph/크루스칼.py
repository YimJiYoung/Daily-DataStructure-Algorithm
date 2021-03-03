# 크루스칼 알고리즘
# 최소 비용으로 만들 수 있는 신장 트리(최소 비용 신장 트리)를 구하는 알고리즘
# 시간 복잡도 O(ElogE) E는 간선의 개수


def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a == b:  # 사이클 발생한 경우 False 반환
        return False
    # 더 작은 쪽 부모로 설정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

    return True


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모  테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 비용이 가장 작은 간선부터 하나씩 확인하며 (Greedy)
for edge in edges:
    cost, a, b = edge
    if union_parent(parent, a, b):  # 사이클 발생하지 않으면 트리에 추가
        result += cost

print(result)
