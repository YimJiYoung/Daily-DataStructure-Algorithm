# 만들 수 없는 금액
# N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하기

n = int(input())
# 코인 오름차순 정렬
coins = sorted(list(map(int, input().split())))
min_coin = 1
# 각 코인에 대해 만들 수 없는 최소 금액 업데이트
for coin in coins:
    # 코인이 최소 금액보다 커지면 최소 금액이 더이상 업데이트 될 일이 없으므로 break
    if coin > min_coin:
        break
    min_coin += coin
print(min_coin)
