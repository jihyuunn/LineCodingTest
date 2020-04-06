import sys
def solution(inputString):
    openString = '({[<'
    closeString = ')}]>'
    opencnt = 0
    pair = 0
    for i in inputString:
        if i in openString:
            opencnt += 1
        elif i in closeString:
            opencnt -= 1
            pair += 1
            if opencnt < 0:
                return -1
    return pair
print(solution('>'))