# <Squares of a Sorted Array>
# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

class Solution(object):
    def sortedSquares(self, A):
        ans = [0]*len(A)
        l, r = 0, len(A) - 1
        i = r
        while (l <= r):
            left, right = abs(A[l]), abs(A[r])
            if (left < right):
                ans[i] = right*right
                r-=1
            else:
                ans[i] = left*left
                l+=1
            i-=1
        return ans
        