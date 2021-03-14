# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163
# 문제를 잘 읽고 풀기 시작하자 ..


from collections import deque


def solution(begin, target, words):
    length = len(begin)
    q = deque([(0, begin)])
    visited = set([begin])

    while q:
        count, cur_word = q.popleft()
        # print(count, cur_word)

        if cur_word == target:
            return count

        for index in range(len(words)):
            word = words[index]
            diff = []
            for pos in range(length):
                if cur_word[pos] != word[pos]:
                    diff.append(pos)
            if len(diff) == 1:
                pos = diff[0]
                next_word = cur_word[:pos] + word[pos] + cur_word[pos+1:]
                if next_word not in visited:
                    q.append((count + 1, next_word))
                    visited.add(next_word)

    return 0
