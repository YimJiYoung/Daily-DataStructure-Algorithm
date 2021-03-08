# 어두운 길
# 최소 신장 트리 문제 -> 크루스칼 알고리즘


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return False
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True


n, m = map(int, input().split(' '))
parent = [x for x in range(n)]
edges = []
save_cost = 0

for _ in range(m):
    x, y, cost = map(int, input().split(' '))
    edges.append((cost, x - 1, y - 1))

edges.sort()

for edge in edges:
    cost, x, y = edge
    if not union_parent(parent, x, y):  # 사이클 발생 -> 비활성화
        save_cost += cost

print(save_cost)
