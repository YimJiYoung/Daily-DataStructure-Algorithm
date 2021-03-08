# 행성 터널
# https://www.acmicpc.net/problem/2887
# 최소 신장 트리 문제
# 임의의 두 노드 사이에 터널 연결할 수 있다고 있으므로 모든 가능한 간선(N*(N-1))를 고려했다가는 시간 초과
# 비용이 min(|Xa - Xb|, |Ya - Yb|, |Za - Zb|)임을 고려하여 각 축(x, y, z)에 대해 정렬하고 배열에서 이웃한 노드들의 간선(3*(N - 1))만을 고려

import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:  # 사이클 발생한 경우 False 반환
        return False
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True


input = sys.stdin.readline
n = int(input())
planets = []
edges = []
parent = [i for i in range(n)]

for i in range(n):
    x, y, z = map(int, input().split(' '))
    planets.append((x, y, z, i))

for axis in [0, 1, 2]:  # x, y, z 좌표 순으로 정렬
    sorted_plantes = sorted(planets, key=lambda x: x[axis])
    for i in range(n - 1):
        cost = abs(sorted_plantes[i][axis] - sorted_plantes[i + 1][axis])
        edges.append((cost, sorted_plantes[i][3], sorted_plantes[i + 1][3]))

edges.sort()
total_cost = 0
tunnel_count = 0

for edge in edges:
    cost, i, j = edge
    if union_parent(parent, i, j):
        total_cost += cost
        tunnel_count += 1
        if tunnel_count >= n - 1:
            break

print(total_cost)
