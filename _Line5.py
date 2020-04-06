def solution(dataSource, tags):
    answer = []
    tagging = [int(x[-1]) for x in tags]
    tagcnt = [0]*10001
    for j in range(len(dataSource)):
        tag = dataSource[j][1:]
        cnt = 0
        for i in range(len(tag)):
            tagNum = int(tag[i][-1])
            if tagNum in tagging:
                cnt += 1
        dataSource[j].append(cnt)
    dataSource = sorted(dataSource, key=lambda x: [x[-1],-int(x[0][-1])], reverse=True)
    for k in (dataSource):
        if k[-1] > 0:
            answer.append(k[0])
    return answer

dataSource = [["doc1", "t1", "t2", "t3"],["doc2", "t0", "t2", "t3"],["doc3", "t1", "t6", "t7"],["doc4", "t1", "t2", "t4"],["doc5", "t6", "t100", "t8"]]
tags = ["t1", "t2", "t3"]
solution(dataSource, tags)