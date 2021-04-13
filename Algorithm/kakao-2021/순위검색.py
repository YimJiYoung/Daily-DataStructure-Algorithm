from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    result = []
    # 조건 그룹 별로 스코어 리스트 저장
    group_by_conditions = defaultdict(list)

    for idx in range(len(info)):
        *conditions, score = info[idx].split(' ')
        for num in range(5):
            # 자신이 속하는 조건의 그룹에 모두 추가 - 조합
            combs = combinations(conditions, num)
            for comb in combs:
                group_by_conditions[comb].append(int(score))

    # 각 그룹별로 스코어 순으로 정렬
    for group in group_by_conditions.values():
        group.sort()

    for q in query:
        *conditions, score = q.replace('and ', '').split(' ')
        valid_conditions = []
        for condition in conditions:
            if condition != '-':
                valid_conditions.append(condition)
        # 검색 조건에 맞는 그룹에서 이진 탐색(bisect_left 이용)으로 score 이상인 개수 카운트
        group = group_by_conditions[tuple(valid_conditions)]
        count = len(group) - bisect_left(group, int(score))
        result.append(count)

    return result
