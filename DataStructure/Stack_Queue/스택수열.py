# 스택 수열
# https://www.acmicpc.net/problem/1874

from collections import deque


def makeSeqence(sequence):
    stack = deque()
    operations = []
    nextNum = 1

    for i in range(n):
        target = sequence[i]

        if target >= nextNum:
            for num in range(nextNum, target + 1):
                stack.append(num)
                operations.append('+')
                nextNum = target + 1

        if not stack or stack[-1] != target:
            return ['NO']

        stack.pop()
        operations.append('-')

    return operations


n = int(input())
sequence = []

for _ in range(n):
    sequence.append(int(input()))

operations = makeSeqence(sequence)

for operation in operations:
    print(operation)
