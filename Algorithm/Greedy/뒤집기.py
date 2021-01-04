# 뒤집기
#  https://www.acmicpc.net/problem/1439
nums = [int(s) for s in input()]
filp_count = [0, 0]  # 전체 문자열을 1과 0로 만들기 위해 뒤집어야 하는 횟수

for i in range(1, len(nums)):
    # 이전 문자열과 다르면 뒤집기 (filp_count 증가)
    if nums[i] != nums[i-1]:
        filp_count[nums[i-1]] += 1
# 마지막 문자에 대한 filp_count 증가
filp_count[nums[-1]] += 1
answer = min(filp_count[0], filp_count[1])
print(answer)
