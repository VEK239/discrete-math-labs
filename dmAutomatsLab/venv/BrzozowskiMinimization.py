import time

class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))

with Profiler() as p:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def reverse(chList, detSet, startSet):
        reversedChList = {}
        for comingPos in chList:
            for letter in chList[comingPos]:
                for goingPos in chList[comingPos][letter]:
                    if goingPos in reversedChList:
                        if letter in reversedChList[goingPos]:
                            reversedChList[goingPos][letter].add(comingPos)
                        else:
                            reversedChList[goingPos][letter] = {comingPos}
                    else:
                        reversedChList[goingPos] = {letter: {comingPos}}
        return reversedChList, startSet, detSet

    def DFAbyNFA(NFAchangesList, NFAdeterminedList, startSet):
        DFAdeterminedList = set()
        DFAchangesList = {}
        DFAbackConditionsMap = {1: startSet}
        posCount = 2
        currPos = [startSet]
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
                            DFAchangesList[conditionNum][letter] = {newCond}
                    else:
                        DFAchangesList[conditionNum] = {letter: {newCond}}
        for condition in DFAbackConditionsMap:
            term = False
            for pos in DFAbackConditionsMap[condition]:
                if pos in NFAdeterminedList:
                    term = True
                    break
            if term:
                DFAdeterminedList.add(condition)
        return DFAchangesList, DFAdeterminedList, {1}

    with open("minimization.in") as inf:
        n, m, k = map(int, inf.readline().split())
        determinedList = set(map(int, inf.readline().split()))
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

    changesList, determinedList, startSet = reverse(changesList, determinedList, {1})
    changesList, determinedList, startSet = DFAbyNFA(changesList, determinedList, startSet)
    changesList, determinedList, startSet = reverse(changesList, determinedList, startSet)
    changesList, determinedList, startSet = DFAbyNFA(changesList, determinedList, startSet)
    with open("minimization.out", "w") as ouf:
        maxPos = 0
        changesCount = 0
        st = ''
        for i in determinedList:
            st += str(i) + ' '
        st += '\n'
        for comingPos in changesList:
            if comingPos > maxPos:
                maxPos = comingPos
            for letter in changesList[comingPos]:
                for goingPos in changesList[comingPos][letter]:
                    if goingPos > maxPos:
                        maxPos = goingPos
                    changesCount += 1
                    st += str(comingPos) + ' ' + str(goingPos) + ' ' + letter + '\n'
        ouf.write(str(maxPos) + ' ' + str(changesCount) + ' ' + str(len(determinedList)) + '\n' + st)