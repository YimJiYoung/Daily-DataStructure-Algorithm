from itertools import combinations

n, m = map(int, input().split(' '))
board = [0]*n

for i in range(n):
    board[i] = list(map(int, input().split(' ')))

homes = []
chickens = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            homes.append((i, j))
        elif board[i][j] == 2:
            chickens.append((i, j))

comb = combinations(chickens, m)


def getChickenDistance(chickens, homes):
    sum = 0
    for home in homes:
        minDist = 2*n
        for chicken in chickens:
            minDist = min(minDist, abs(
                home[0] - chicken[0]) + abs(home[1] - chicken[1]))
        sum += minDist
    return sum


minChickenDistance = float('inf')

for candidate in comb:
    minChickenDistance = min(
        minChickenDistance, getChickenDistance(candidate, homes))

print(minChickenDistance)
