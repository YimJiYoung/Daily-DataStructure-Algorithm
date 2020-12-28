# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2

#     if array[mid] == target:
#         return mid
#     # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
#     else:
#         return binary_search(array, target, mid + 1, end)

# while문


def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(array, 5))
