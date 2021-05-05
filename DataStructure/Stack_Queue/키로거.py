# 키로거
# https://www.acmicpc.net/problem/5397
# Stack 2개 이용


def getKey(s):
    beforeCursor = []
    afterCursor = []
    for token in s:
        if token == '>':
            if afterCursor:
                beforeCursor.append(afterCursor.pop())
        elif token == '<':
            if beforeCursor:
                afterCursor.append(beforeCursor.pop())
        elif token == '-':
            if beforeCursor:
                beforeCursor.pop()
        else:
            beforeCursor.append(token)
    return "".join(beforeCursor) + "".join(reversed(afterCursor))


testCaseNum = int(input())

for _ in range(testCaseNum):
    s = input()
    key = getKey(s)
    print(key)
