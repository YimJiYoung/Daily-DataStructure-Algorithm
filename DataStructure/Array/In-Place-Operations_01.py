# In-place Array operations are where we modify an Array, without creating a new Array.

# <Replace Elements with Greatest Element on Right Side>
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        length = len(arr)
        mi = -1 # max index
        for i in range(length):
            if (i == length -1):
                arr[i] = -1
                break
            # find new max index from its right
            if (i >= mi) :
                mi = i+1
                for j in range(i+2, length):
                    if arr[j] > arr[mi]:
                        mi = j
            # replace with max value
            arr[i] = arr[mi]
        return arr


# Good answer by lee215
# def replaceElements(self, A, mx = -1):
#     for i in xrange(len(A) - 1, -1, -1):
#         A[i], mx = mx, max(mx, A[i])
#     return A