alphabet = 'abcdefghijklmnopqrstuvwxyz'

DFAdeterminedList = set()
DFAchangesList = {}
DFAbackConditionsMap = {1: {1}}

def count():
    currPos = {1: 1}
    for i in range(l):
        newCurrPos = {}
        if len(currPos) == 0:
            break
        for comingIndex in currPos:
            sum = currPos[comingIndex]
            if comingIndex in DFAchangesList:
                tmpList = DFAchangesList[comingIndex]
                for letter in tmpList:
                    goingIndex = tmpList[letter]
                    if goingIndex in newCurrPos:
                        newCurrPos[goingIndex] += sum
                    else:
                        newCurrPos[goingIndex] = sum
        currPos = newCurrPos
    wordCount = 0
    for pos in currPos:
        if pos in DFAdeterminedList:
            wordCount += currPos[pos]
    return wordCount

def DFAbyNFA():
    posCount = 2
    currPos = [{1}]
    while len(currPos) > 0:
        tmpSet = currPos.pop(0)
        for key in DFAbackConditionsMap:
            if DFAbackConditionsMap[key] == tmpSet:
                conditionNum = key
                break
        for letter in alphabet:
            resultingSet = set()
            for tmp in tmpSet:
                if tmp in NFAchangesList and letter in NFAchangesList[tmp]:
                    resultingSet = resultingSet.union(NFAchangesList[tmp][letter])
            if len(resultingSet) > 0:
                if resultingSet not in DFAbackConditionsMap.values():
                    DFAbackConditionsMap[posCount] = resultingSet
                    posCount += 1
                    currPos.append(resultingSet)
                for key in DFAbackConditionsMap:
                    if DFAbackConditionsMap[key] == resultingSet:
                        newCond = key
                        break
                if conditionNum in DFAchangesList:
                    if letter not in DFAchangesList[conditionNum]:
                        DFAchangesList[conditionNum][letter] = newCond
                else:
                    DFAchangesList[conditionNum] = {letter: newCond}
    for condition in DFAbackConditionsMap:
        term = False
        for pos in DFAbackConditionsMap[condition]:
            if pos in NFAdeterminedList:
                term = True
                break
        if term:
            DFAdeterminedList.add(condition)

with open("problem5.in") as inf:
    n, m, k, l = map(int, inf.readline().split())
    NFAdeterminedList = list(map(int, inf.readline().split()))
    NFAchangesList = {}
    for i in range(m):
        tmp = inf.readline().split()
        if int(tmp[0]) in NFAchangesList:
            if tmp[2] in NFAchangesList[int(tmp[0])]:
                NFAchangesList[int(tmp[0])][tmp[2]].add(int(tmp[1]))
            else:
                NFAchangesList[int(tmp[0])][tmp[2]] = {int(tmp[1])}
        else:
            NFAchangesList[int(tmp[0])] = {tmp[2]: {int(tmp[1])}}
DFAbyNFA()

with open("problem5.out", "w") as ouf:
    ouf.write(str(count() % (1000000000 + 7)))
