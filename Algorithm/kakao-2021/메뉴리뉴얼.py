from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    comb_count_by_course = [defaultdict(
        int) for _ in range(len(course))]  # 코스 별 가능한 메뉴 후보

    for order in orders:
        for i in range(len(course)):
            size = course[i]
            if len(order) < size:
                break
            possible_combs = combinations(sorted(order), size)
            for comb in possible_combs:
                comb_count_by_course[i][comb] += 1

    result = []

    for comb_count in comb_count_by_course:
        sorted_comb_count = sorted(
            comb_count.items(), key=lambda x: x[1], reverse=True)
        if len(sorted_comb_count) == 0 or sorted_comb_count[0][1] < 2:
            continue
        max_count = sorted_comb_count[0][1]
        for comb, count in sorted_comb_count:
            if count == max_count:
                result.append(''.join(comb))
            else:
                break

    return sorted(result)
