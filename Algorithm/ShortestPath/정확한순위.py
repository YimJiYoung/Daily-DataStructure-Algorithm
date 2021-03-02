# 정확한 순위
# 성적 순위를 정확히 알 수 있는 학생 모두 몇 명인지 계산
# 성적 순위를 정확히 알 수 있다 = 다른 모든 노드와 연결되어 있다

n, m = map(int, input().split(' '))

# 학생간의 연결 상태 true/false로 저장
graph = [[False] * n for _ in range(n)]

for _ in range(m):
    src, dst = map(int, input().split(' '))
    graph[src - 1][dst - 1] = True

for i in range(n):
    graph[i][i] = True

# 플로이드 워셜 알고리즘
for k in range(n):
    for a in range(n):
        for b in range(n):
            # k 노드 거쳐서 갈 수 있는지 확인
            if graph[a][k] and graph[k][b]:
                graph[a][b] = True

# 성적 순위 확실히 알 수 있는 학생 확인
count = 0
for target in range(n):
    knowable = True
    for other in range(n):
        if not graph[target][other] and not graph[other][target]:
            knowable = False
    if knowable:
        count += 1

print(count)
