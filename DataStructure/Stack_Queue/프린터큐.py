# 프린터 큐
# https://www.acmicpc.net/problem/1966
# 데이터의 개수가 적으므로 문제에서 요구하는대로 푼다.

from collections import deque

testCaseNum = int(input())

for _ in range(testCaseNum):
    n, m = map(int, input().split(' '))
    documents = list(map(int, input().split(' ')))
    documents = deque([(value, index)
                       for index, value in enumerate(documents)])

    count = 1
    while documents:
        maxDocument = max(documents)
        if documents[0][0] != maxDocument[0]:
            documents.rotate(-1)
        else:
            poped = documents.popleft()
            if poped[1] == m:
                print(count)
                break
            count += 1
