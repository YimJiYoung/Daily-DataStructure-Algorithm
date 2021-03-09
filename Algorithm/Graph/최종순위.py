# 최종 순위
# https://www.acmicpc.net/problem/3665


from collections import deque


def change_rank(a, b):  # a보다 b가 더 높은 순위
    indegree[a] -= 1
    indegree[b] += 1
    graph[b].remove(a)
    graph[a].append(b)


def topology_sort(indegree, graph):
    q = deque()
    result = []
    certain = True

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        if len(q) > 1:  # 여러 경우의 수가 가능한 경우 -> 확실한 순위 만들 수 없는 경우
            certain = False
            break
        node = q.popleft()
        result.append(node)

        for next_node in graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                q.append(next_node)

    if not certain:
        print('?')
    elif len(result) != len(indegree) - 1:
        print("IMPOSSIBLE")
    else:
        for team in result:
            print(team, end=" ")


t = int(input())

for _ in range(t):
    n = int(input())
    indegree = [0] * (n + 1)
    rankOf = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    ranking = list(map(int, input().split(' ')))

    for i in range(n):
        indegree[ranking[i]] = i
        rankOf[ranking[i]] = i + 1
        graph[ranking[i]] = ranking[i + 1:]

    m = int(input())
    for _ in range(m):
        # 바뀐 두 순위
        a, b = map(int, input().split(' '))
        if rankOf[a] > rankOf[b]:
            change_rank(a, b)
        else:
            change_rank(b, a)

    topology_sort(indegree, graph)
