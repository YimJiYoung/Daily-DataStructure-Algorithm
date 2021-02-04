# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

n = int(input())
numbers = list(map(int, input().split(' ')))
operators = list(map(int, input().split(' ')))  # + - x /

min_value = float('inf')
max_value = float('-inf')


def compute(now, index, operators):
    global min_value, max_value

    if index == len(numbers):  # 모든 연산자 삽입 결과로 최대값, 최소값 업데이트
        min_value = min(min_value, now)
        max_value = max(max_value, now)
        return

    if operators[0] > 0:  # +
        operators[0] -= 1
        compute(now + numbers[index], index + 1, operators)
        operators[0] += 1
    if operators[1] > 0:  # -
        operators[1] -= 1
        compute(now - numbers[index], index + 1, operators)
        operators[1] += 1
    if operators[2] > 0:  # x
        operators[2] -= 1
        compute(now * numbers[index], index + 1, operators)
        operators[2] += 1
    if operators[3] > 0:  # /
        if numbers[index] != 0:
            operators[3] -= 1
            compute(int(now / numbers[index]), index + 1, operators)
            operators[3] += 1


compute(numbers[0], 1, operators)

print(max_value)
print(min_value)
