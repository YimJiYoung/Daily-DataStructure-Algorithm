# 탑승구
# key: 가능한 큰 번호의 탑승구로 도킹한다 -> 서로소 알고리즘 이용 (경로 압축으로 인한 시간 복잡도 감소 / 도킹하는 과정 이전 게이트와의 합집합 연산으로 처리)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def dock(parent, gate):
    gate = find_parent(parent, gate)
    if gate == 0:  # 도킹 가능한 게이트가 없음
        return False
    parent[gate] = find_parent(parent, gate - 1)  # 이전 게이트 노드로 연결
    return True


G = int(input())
P = int(input())

possibleGate = [0] * P
parent = [x for x in range(G + 1)]
count = 0

for i in range(P):
    possibleGate[i] = int(input())

for i in range(P):
    if not dock(parent, possibleGate[i]):
        break
    count += 1

print(count)
