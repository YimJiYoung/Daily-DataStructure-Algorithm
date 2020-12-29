# 정수 삼각형
# https://www.acmicpc.net/problem/1932

n = int(input())
triangle = []
d = []  # dp를 위한 테이블
for _ in range(n):
    line = list(map(int, input().split()))
    triangle.append(line)
    d.append([0]*len(line))

# 마지막 줄에 대한 d 값 삼각형의 값으로 설정
for i in range(len(triangle[n-1])):
    d[n-1][i] = triangle[n-1][i]

# dp로 마지막에서 두 번째 줄부터 올라오면서 계산
for i in reversed(range(n-1)):
    for j in range(len(triangle[i])):
        d[i][j] = triangle[i][j] + max(d[i+1][j], d[i+1][j+1])

print(d[0][0])
