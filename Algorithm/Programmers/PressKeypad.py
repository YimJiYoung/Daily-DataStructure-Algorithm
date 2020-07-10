# [카카오 인턴] 키패드 누르기

def solution(numbers, hand):
    answer = ''
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    lpos, rpos = [0, 3], [2, 3]
    for n in numbers:
        # 왼쪽
        if n in [1, 4, 7]:
            answer+='L'
            lpos = [0, n//3]
        # 오른쪽
        elif n in [3, 6, 9]:
            answer+='R'
            rpos =[2, n//3 - 1]
        # 가운데
        else:
            npos = [1, 3 if n == 0 else n//3]
            # 거리 계산
            ldis = abs(lpos[0] - npos[0]) + abs(lpos[1] - npos[1])
            rdis = abs(rpos[0] - npos[0]) + abs(rpos[1] - npos[1])
            if (ldis < rdis or (ldis == rdis and hand =='left')):
                answer += 'L'
                lpos = npos
            elif (ldis > rdis or (ldis == rdis and hand =='right')):
                answer += 'R'
                rpos = npos 
    return answer