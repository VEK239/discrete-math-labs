with open("problem4.in") as inf:
    n, m, k, l = map(int, inf.readline().split())
    determinedList = list(map(int, inf.readline().split()))
    changesList = {}
    for i in range(m):
        tmp = inf.readline().split()
        if int(tmp[0]) in changesList:
            if tmp[2] in changesList[int(tmp[0])]:
                changesList[int(tmp[0])][tmp[2]].add(int(tmp[1]))
            else:
                changesList[int(tmp[0])][tmp[2]] = {int(tmp[1])}
        else:
            changesList[int(tmp[0])] = {tmp[2]: {int(tmp[1])}}
#print(changesList)
currPos = {1: 1}  #{2: 4 ; 5: 3; 1: 2}
for i in range(l):
    #print("currPos: ", currPos)
    newCurrPos = {}
    if len(currPos) == 0:
        break
    for comingIndex in currPos:
        sum = currPos[comingIndex]
        if comingIndex in changesList:
            tmpList = changesList[comingIndex]
            #print("tmp: ", tmpList)
            for letter in tmpList:
                goingList = tmpList[letter]
                for goingIndex in goingList:
                    if goingIndex in newCurrPos:
                        newCurrPos[goingIndex] += sum
                    else:
                        newCurrPos[goingIndex] = sum
    #print("newCurrPos: ", newCurrPos, "\n")
    currPos = newCurrPos
wordCount = 0
for pos in currPos:
    if pos in determinedList:
        wordCount += currPos[pos]
with open("problem4.out", "w") as ouf:
    ouf.write(str(wordCount % (1000000000 + 7)))
