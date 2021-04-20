# 문자열 뒤집기
# https://www.acmicpc.net/problem/1439


def solutioin(nums):
    length = len(nums)

    if length == 0:
        return 0

    group_count = [0] * 2

    for i in range(1, length):
        if nums[i] != nums[i - 1]:
            group_count[nums[i - 1]] += 1
    group_count[nums[-1]] += 1

    return min(group_count)


nums = [int(s) for s in input()]
print(solutioin(nums))
