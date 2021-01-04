# 왼쪽부터 오르쪽으로 하나씩 모둔 숫자를 확인하며 숫자 사이에 x 또는 + 연산자를 넣어 만들 수 있는 가장 큰 수 구하기

nums = input()
result = int(nums[0])
for i in range(1, len(nums)):
    # x + 했을 때의 결과 비교하여 큰 값을 취한다
    result = max(result * int(nums[i]), result + int(nums[i]))
print(result)
