# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058


def validate(p):
    count = 0
    for c in p:
        if c == ')':
            if count == 0:
                return False
            count -= 1
        else:
            count += 1
    if count != 0:
        return False
    return True


def getBalancedIndex(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def correct(p):
    if p == '':
        return p

    index = getBalancedIndex(p)
    u = p[:index+1]
    v = p[index+1:]

    # u가 올바른 괄호 문자열인 경우 수행 결과 u에 이어 붙여 반환
    if validate(u):
        return u + correct(v)

    # u가 올바른 괄호 문자열이 아닌 경우
    # 빈 문자열에 '('와 v 수행 결과 ')' 이어 붙이기
    answer = '(' + correct(v) + ')'
    # u 괄호 방향 뒤집은 문자열 붙이기
    flip = {
        '(': ')',
        ')': '('
    }
    answer += ''.join([flip[c] for c in u[1:-1]])
    return answer


def solution(p):
    if validate(p):
        return p
    return correct(p)


# 내 해석대로 생각하지 말고 문제를 잘보고 문제에서 구현하란 대로 구현하자 !
