import sys

input = sys.stdin.readline


n = int(input())
scores = []

# for _ in range(n):
#     name, lang, eng, math = input().split(' ')
#     scores.append((-int(lang), int(eng), -int(math), name))

# scores.sort()

# key 속성 사용하여 배열 정렬

for _ in range(n):
    name, lang, eng, math = input().split(' ')
    scores.append((name, int(lang), int(eng), int(math)))

scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for score in scores:
    print(score[0])
