def usefulDfs(currPos):
    # print(currPos)
    usefulList[currPos - 1] = True
    visitedList[currPos - 1] = True
    if currPos != 1 and currPos in backChangesList:
        for goingPos in backChangesList[currPos]:
            if not visitedList[goingPos - 1]:
                usefulDfs(goingPos)

def cicles(currPos, attended):
    if usefulList[currPos - 1]:
        if currPos in attended:
            return True
        newAttended = attended.copy()
        newAttended.add(currPos)
        result = False
        if currPos in changesList:
            res = changesList[currPos]
            for letter in res:
                result = result or cicles(res[letter], newAttended)
        return result
    else:
        return False

def count():
    wordCount = 0
    currPos = {1: 1}
    while len(currPos) > 0:
        newCurrPos = {}
        for comingIndex in currPos:
            if usefulList[comingIndex - 1]:
                sum = currPos[comingIndex]
                if comingIndex in determinedList:
                    wordCount += sum
                if comingIndex in changesList:
                    goingList = changesList[comingIndex]
                    for goingLetter in goingList:
                        goingPos = changesList[comingIndex][goingLetter]
                        if goingPos in newCurrPos:
                            newCurrPos[goingPos] += sum
                        else:
                            newCurrPos[goingPos] = sum
        currPos = newCurrPos
    return wordCount


with open("problem3.in") as inf:
    n, m, k = map(int, inf.readline().split())
    determinedList = set(map(int, inf.readline().split()))
    changesList = {}
    backChangesList = {}
    for i in range(m):
        tmp = inf.readline().split()
        if int(tmp[0]) in changesList:
            changesList[int(tmp[0])][tmp[2]] = int(tmp[1])
        else:
            changesList[int(tmp[0])] = {tmp[2]: int(tmp[1])}
        if int(tmp[1]) in backChangesList:
            backChangesList[int(tmp[1])].add(int(tmp[0]))
        else:
            backChangesList[int(tmp[1])] = {int(tmp[0])}

# print(backChangesList)
usefulList = [False for i in range(n)]
visitedList = [False for i in range(n)]
for d in determinedList:
    usefulDfs(d)

# print(usefulList)
with open("problem3.out", "w") as ouf:
    if cicles(1, set()):
        ouf.write("-1")
    else:
        ouf.write(str(count() % (1000000000 + 7)))