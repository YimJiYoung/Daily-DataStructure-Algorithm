import re

def solution(dartResult):
    bonusSymbol = { 'S': 1, 'D': 2, 'T': 3 }
    optionSymbol = { '': 1, '*': 2, '#': -1 }
    p = re.compile('(\d+)([SDT])([\*#])?')
    scoreStrList = p.findall(dartResult)
    scoreList = []
    for base, bonus, option in scoreStrList:
        if (option == '*' and len(scoreList)>0):
            scoreList[-1] *= 2
        score = int(base)**bonusSymbol[bonus]*optionSymbol[option]
        scoreList.append(score)
    answer = sum(scoreList)
    return answer