def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        binStr = bin(num1|num2)[2:].rjust(n, '0')
        symbolStr = binStr.replace('1', '#')
        symbolStr = symbolStr.replace('0', ' ')
        answer.append(symbolStr)
    return answer