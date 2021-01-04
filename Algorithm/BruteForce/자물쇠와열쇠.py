# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3


# 2차원 배열 90도 회전
def rotate(arr):
    return list(zip(*arr[::-1]))


# 완전 탐색으로 풀기
def solution(key, lock):
    n = len(lock)
    m = len(key)
    lock_count = 0

    # lock m만큼 확장한 board 배열 초기화
    board = [[-1] * (n + 2*m) for _ in range(n + 2*m)]
    for i in range(m, n+m):
        for j in range(m, n+m):
            if lock[i-m][j-m] == 0:
                lock_count += 1
            board[i][j] = lock[i-m][j-m]

    # 완전 탐색
    for _ in range(4):  # 회전
        for i in range(1, n + m):  # board i, j 위치 고정
            for j in range(1, n + m):
                solve_count = 0
                for a in range(m):
                    for b in range(m):
                        if (board[i+a][j+b] == 0 and key[a][b] == 0) or (board[i+a][j+b] == 1 and key[a][b] == 1):
                            break
                        if board[i+a][j+b] == 0 and key[a][b] == 1:
                            solve_count += 1
                if solve_count == lock_count:  # lock count 만큼 풀렸다 !
                    return True
        key = rotate(key)

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
               [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	))
