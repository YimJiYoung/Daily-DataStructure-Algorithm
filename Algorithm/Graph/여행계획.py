# 여행 계획
# '여행 계획'에 해당하는 모든 노드가 같은 집합에 속하면(=연결되어 있다면) 가능한 여행 경로


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


def check_plan(parent, plan):
    for i in range(m - 1):
        if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):  # 연결되어 있지 않음
            return False
    return True


n, m = map(int, input().split(' '))
graph = []
parent = [i for i in range(n)]

for i in range(n):
    row = list(map(int, input().split(' ')))
    graph.append(row)
    for j in range(n):
        if graph[i][j] == 1:  # 노드가 연결된 경우
            union_parent(parent, i, j)

plan = list(map(int, input().split(' ')))

if check_plan(parent, plan):
    print('YES')
else:
    print('NO')
