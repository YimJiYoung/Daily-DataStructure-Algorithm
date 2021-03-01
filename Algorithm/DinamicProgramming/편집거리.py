from collections import deque

source = input()
target = input()

# bfs로 탐색

# q = deque([(source, target)])
# distance = 0

# while q:
#     size = len(q)

#     for _ in range(size):
#         src, dst = q.popleft()
#         print(distance, src, dst)

#         if src == dst:
#             print(distance)
#             exit(0)

#         for i in range(min(len(src), len(dst))):
#             if src[i] != dst[i]:
#                 # 삽입
#                 q.append((src[i:], dst[i + 1:]))
#                 # 삭제
#                 q.append((src[i + 1:], dst[i:]))
#                 # 교체
#                 q.append((src[i + 1:], dst[i + 1:]))
#                 break

#     distance += 1

targetLength = len(target)
sourceLength = len(source)

# 편집 거리를 담은 2차원 테이블 - dp[i][j] source[:i+1]에서 target[:j+1]을 만드는 편집 거리
dp = [[None] * (targetLength + 1) for _ in range(sourceLength + 1)]

for i in range(sourceLength + 1):
    dp[i][0] = i

for j in range(targetLength + 1):
    dp[0][j] = j

for i in range(1, sourceLength + 1):
    for j in range(1, targetLength + 1):
        # 행과 열에 해당하는 문자가 같은 경우
        if source[i - 1] == target[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        # 문자 다른 경우
        else:
            # 삽입, 삭제, 교체 중 가장 작은 편집 거리 선택
            dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

print(dp[sourceLength][targetLength])
