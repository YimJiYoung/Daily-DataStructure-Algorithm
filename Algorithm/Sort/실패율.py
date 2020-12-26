# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    fail_rate = []
    length = len(stages)
    for i in range(1, N+1):
        if length == 0:
            for j in range(i, N+1):
                fail_rate.append((0, j))
            break
        fail_count = stages.count(i)
        fail_rate.append((-1*fail_count/length, i))
        length -= fail_count
    fail_rate.sort()
    return list(map(lambda x: x[1], fail_rate))


# 처음 풀이
# 굳이 filter와 sum으로 비슷한 연산을 반복해서 시간적으로 비효울적이었음
# def solution(N, stages):
#     failRate = []
#     for i in range(1, N+1):
#         stages = list(filter(lambda x: x >= i, stages))
#         if len(stages):
#             failRate.append((0, i))
#             continue
#         failCount = sum(stage == i for stage in stages)
#         clearCount = len(stages) - failCount
#         failRate.append((-1*failCount/(failCount + clearCount), i))
#     failRate.sort()
#     return list(map(lambda x: x[1], failRate))
