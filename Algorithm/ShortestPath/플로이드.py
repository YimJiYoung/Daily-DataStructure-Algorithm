# 플로이드
# https://www.acmicpc.net/problem/11404

import sys
import math
input = sys.stdin.readline

n = int(input())
m = int(input())

# 최단 경로 테이블
graph = [[float('inf')]*n for i in range(n)]

# 자기 자신에 대한 경로 0으로 설정
for i in range(n):
    graph[i][i] = 0

# 모든 버스 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 노드에서 b 노드로 가는 비용이 c라는 의미
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

# 플로이드 워셜 알고리즘
for k in range(n):
    for a in range(n):
        for b in range(n):
            # k 노드 거치는 경로의 길이와 비교
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 출력
for a in range(n):
    for b in range(n):
        if math.isinf(graph[a][b]):
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
