class Solution(object):
    # Using Dynamic Programing
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        cntPerfectSquares = [float('inf')]*(n+1)
        cntPerfectSquares[0] = 0
        for i in range(1, n+1) :
            sqrt = int(math.sqrt(i))
            for j in range(sqrt, 0, -1):
                cntPerfectSquares[i] = min(cntPerfectSquares[i], cntPerfectSquares[i - j*j] + 1)
        return cntPerfectSquares[n]

    #Using Static Dynamic Programming
    # cntPerfectSquares = [0]
    # def numSquares(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     length = len(Solution.cntPerfectSquares)
    #     if length > n+1:
    #         return Solution.cntPerfectSquares[n]
        
    #     for i in range(length, n+1) :
    #         sqrt = int(math.sqrt(i))
    #         cnt = float('inf')
    #         for j in range(sqrt, 0, -1):
    #             cnt = min(cnt, Solution.cntPerfectSquares[i - j*j] + 1)
    #         Solution.cntPerfectSquares.append(cnt)
    #     return Solution.cntPerfectSquares[n]

    # Using BFS
    # def numSquares(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     # perfect squares smallar than n
    #     sqrt = int(math.sqrt(n))
    #     perfectSquares = [i*i for i in range(1, sqrt + 1)]

    #     toCheck = {n}
    #     cnt = 0

    #     while toCheck:
    #         nextCheck = set()
    #         for m in toCheck :
    #             print(m, cnt)
    #             if m == 0:
    #                 return cnt
    #             for square in perfectSquares:
    #                 if (m - square >= 0):
    #                     nextCheck.add(m - square)
    #         toCheck = nextCheck
    #         cnt += 1

    #     return cnt

