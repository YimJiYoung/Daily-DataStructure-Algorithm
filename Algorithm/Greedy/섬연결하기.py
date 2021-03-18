# 섬 연결하기
# https://programmers.co.kr/learn/courses/30/lessons/42861


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:  # 같은 집합 -> 사이클 발생
        return False
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True


def solution(n, costs):
    graph = [[float('inf')] * n for _ in range(n)]
    edges = []
    parent = [x for x in range(n)]  # 연결된 집합 정보

    for a, b, cost in costs:
        graph[a][b] = cost
        graph[b][a] = cost
        edges.append((cost, a, b))

    edges.sort()
    total_cost = 0
    briedge_count = 0

    # 가장 짧은 간선 순서로 선택
    for edge in edges:
        cost, a, b = edge

        if union_parent(parent, a, b):
            total_cost += cost
            briedge_count += 1
            if briedge_count == n - 1:
                break

    return total_cost
