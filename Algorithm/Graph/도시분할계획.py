# 도시 분할 계획
# https://www.acmicpc.net/problem/1647
# 2개의 최소 신장 트리 -> 하나의 최소 신장 트리 만들고 비용이 가장 큰 간선 제거

import sys


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


input = sys.stdin.readline
n, m = map(int, input().split(' '))
edges = []
parent = [i for i in range(n)]
costs = []  # 이어진 신장 트리의 비용

for _ in range(m):
    a, b, cost = map(int, input().split(' '))
    edges.append((cost, a - 1, b - 1))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클 발생하지 않을 때
    if union_parent(parent, a, b):
        costs.append(cost)

print(sum(costs[:-1]))
