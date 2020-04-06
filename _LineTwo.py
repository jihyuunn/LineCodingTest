import sys
def compare(first, second, answerSheet):
    n = len(first)
    total = 0
    check = [0]*n
    for i in range(n):
        if first[i]!= answerSheet[i] and first[i] == second[i]:
            check[i] = check[i-1]+1
            total += 1
    print(check, total)
    return total, max(check)
    
def solution(answer_sheet, sheets):
    answer = -1
    n = len(answerSheet)
    m = len(sheet)
    # wrong = [[0]*n for _ in range(m)]
    # for i in range(m):
    #     cur = sheet[i]
    #     for j in range(n):
    #         if cur[j] != answerSheet[j]:
    #             wrong[i][j] = cur[j]
    # print(wrong)
    maxx = 0
    for k in range(m):
        for z in range(k+1, m):
            total, long = compare(sheet[k], sheet[z], answerSheet)
            maxx = max(maxx, total+(long**2))
    print(maxx)
    return answer
answerSheet = "4132315142"
sheet = ["3241523133","4121314445","3243523133","4433325251","2412313253"]
solution(answerSheet, sheet)
