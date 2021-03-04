# 커리큘렴
# N개의 강의 정보가 주어졌을 때, N개의 강의에 대하여 수강하기까지 걸리는 최소 시간 출렬
# 위상정렬 알고리즘 응용

from collections import deque

n = int(input())
graph = [[] for _ in range(n)]
indegree = [0] * n
duration = [0] * n

for i in range(n):
    time, *prerequisites = list(map(int, input().split(' ')))
    duration[i] = time
    for prerequisite in prerequisites:
        if prerequisite != -1:
            graph[prerequisite - 1].append(i)
            indegree[i] += 1

result = duration[:]  # 최종적으로 각 강의를 수강하기까지의 최소 시간
queue = deque()

for i in range(n):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    course = queue.popleft()

    for next_course in graph[course]:
        # 최소 강의 시간 업데이트
        result[next_course] = max(
            result[next_course], result[course] + duration[next_course])
        indegree[next_course] -= 1
        if indegree[next_course] == 0:
            queue.append(next_course)

for min_time in result:
    print(min_time)
