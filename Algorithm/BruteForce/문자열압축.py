def solution(s):
    length = len(s)
    min_length = length
    for step in range(1, int(length/2) + 1):
        i = 0
        repeat_count = 1
        repeat_str = s[:step]
        compressed = ''
        for i in range(step, length, step):
            if s[i: i+step] == repeat_str:  # 이전 문자열이 반복되는 경우
                repeat_count += 1
            else:  # 이전 문자열이 반복되지 않는 경우
                if repeat_count > 1:  # 압축된 경우
                    compressed += str(repeat_count)
                compressed += repeat_str
                repeat_str = s[i: i+step]
                repeat_count = 1
        # 남아 있는 문자열 더하기
        if repeat_count > 1:
            compressed += str(repeat_count)
        compressed += repeat_str

        min_length = min(len(compressed), min_length)

    return min_length
