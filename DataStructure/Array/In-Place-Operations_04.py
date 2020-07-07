# <Sort Array By Parity>
# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = A[:]
        even_length = 0
        for i in range(len(A)):
            if (A[i] % 2 == 0):
                even_length += 1
        ei = 0
        oi = even_length    
        for i in range(len(A)):
            if (A[i] % 2 == 0):
                ans[ei] = A[i]
                ei += 1
            else:
                ans[oi] = A[i]
                oi += 1
        return ans
        
        # short version
        # return [x for x in A if x%2 == 0] + [x for x in A if x%2 != 0]
        
        # use quick sort
        # left, right = 0, len(A)-1
        # while (left <= right):
        #     while (left <= right and A[left]%2==0):
        #         left+=1
        #     while (left <= right and A[right]%2==1):
        #         right-=1
        #     if (left <= right):
        #         A[left],A[right] = A[right], A[left]      
        # return A