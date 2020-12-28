# 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right


# bisect 함수를 이용하여 이진 탐색으로(logN) 특정 범위에 해당하는 데이터 개수 반환
def count_by_range(arr, left_value, right_value):
    left_index = bisect_left(arr, left_value)
    right_index = bisect_right(arr, right_value)
    return right_index - left_index


def solution(words, queries):
    answer = [0]*len(queries)

    # 단어 길이 별로 저장
    words_by_length = [[] for _ in range(10001)]
    words_by_length_reverse = [[] for _ in range(10001)]

    for word in words:
        words_by_length[len(word)].append(word)
        words_by_length_reverse[len(word)].append(word[::-1])

    # 이진 탐색을 위한 정렬
    for i in range(10001):
        words_by_length[i].sort()
        words_by_length_reverse[i].sort()

    for idx, query in enumerate(queries):
        length = len(query)
        # '?'로만 되어 있는 경우 해당 길이의 단어 개수가 답이 된다
        if query == '?'*length:
            answer[idx] += len(words_by_length[length])
            continue
        # '?'가 접미사인 경우
        if query[0] != '?':
            left_value = query.replace('?', 'a')
            right_value = query.replace('?', 'z')
            answer[idx] += count_by_range(words_by_length[length],
                                          left_value, right_value)
        # '?'가 접두사인 경우 -> 뒤집은 배열에 대해 탐색
        else:
            reversed_query = query[::-1]
            left_value = reversed_query.replace('?', 'a')
            right_value = reversed_query.replace('?', 'z')
            answer[idx] += count_by_range(words_by_length_reverse[length],
                                          left_value, right_value)

    return answer
