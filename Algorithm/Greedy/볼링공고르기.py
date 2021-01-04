n, m = list(map(int, input().split()))
balls = list(map(int, input().split()))
# index만큼의 무게를 가진 공의 개수
ball_count = [0] * (m + 1)
# 두 사람이 고를 수 있는 볼링 공 조합 - 초기값 : 무게 따지지 않은 모든 조합으로 설정
comb_count = (n * (n - 1)) / 2

for ball in balls:
    ball_count[ball] += 1

for count in ball_count:  # 같은 무게의 볼링공 선택할 수 없으므로 경우의 수에서 제외
    comb_count -= (count * (count - 1)) / 2

print(comb_count)
