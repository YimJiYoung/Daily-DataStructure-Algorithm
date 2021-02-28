# 못생긴 수 - 오직 2, 3, 5를 약수로 가지는 합성수

n = int(input())
uglyNums = [0] * n
uglyNums[0] = 1

# 기존의 못생긴 수에 2, 3, 5를 곱하며 다음으로 가능한 못생긴 수 담는 변수
next2 = 2
next3 = 3
next5 = 5

# 2, 3, 5를 곱한 못생긴 수의 index
i2 = i3 = i5 = 0

for i in range(1, n):
    uglyNums[i] = min(next2, next3, next5)

    if uglyNums[i] == next2:
        i2 += 1
        next2 = uglyNums[i2] * 2

    if uglyNums[i] == next3:
        i3 += 1
        next3 = uglyNums[i3] * 3

    if uglyNums[i] == next5:
        i5 += 1
        next5 = uglyNums[i5] * 5

print(uglyNums[n - 1])
