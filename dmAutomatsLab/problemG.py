alphabet = 'abcdefghijklmnopqrstuvwxyz'


def correct():
    currPos = [[1, 1]]
    while len(currPos) > 0:
        res = currPos.pop(0)
        u = res[0]
        v = res[1]
        if (u in firstDeterminedList) ^ (v in secondDeterminedList):
            return False
        if u in firstChangesList:
            firstVisit[u - 1] = True
        if v in secondChangesList:
            secondVisit[v - 1] = True
        for letter in alphabet:
            if u in firstChangesList and letter in firstChangesList[u]:
                if v in secondChangesList and letter in secondChangesList[v]:
                    point = secondChangesList[v][letter]
                else:
                    point = secondDeadPoint
                if not (firstVisit[firstChangesList[u][letter] - 1] and secondVisit[point - 1]):
                    currPos.append([firstChangesList[u][letter], point])
            else:
                if v in secondChangesList and letter in secondChangesList[v]:
                    if not (firstVisit[firstDeadPoint - 1] and secondVisit[secondChangesList[v][letter] - 1]):
                        currPos.append([firstDeadPoint, secondChangesList[v][letter]])
    return True


with open("equivalence.in") as inf:
    n, m, k = map(int, inf.readline().split())
    firstDeterminedList = set(map(int, inf.readline().split()))
    firstChangesList = {}
    for i in range(m):
        tmp = inf.readline().split()
        if int(tmp[0]) in firstChangesList:
            firstChangesList[int(tmp[0])][tmp[2]] = int(tmp[1])
        else:
            firstChangesList[int(tmp[0])] = {tmp[2]: int(tmp[1])}
    firstDeadPoint = n + 1
    firstVisit = [False for i in range(n + 1)]

    n, m, k = map(int, inf.readline().split())
    secondDeterminedList = set(map(int, inf.readline().split()))
    secondChangesList = {}
    for i in range(m):
        tmp = inf.readline().split()
        if int(tmp[0]) in secondChangesList:
            secondChangesList[int(tmp[0])][tmp[2]] = int(tmp[1])
        else:
            secondChangesList[int(tmp[0])] = {tmp[2]: int(tmp[1])}
    secondDeadPoint = n + 1
    secondVisit = [False for i in range(n + 1)]

with open("equivalence.out", "w") as ouf:
    if correct():
        ouf.write("YES")
    else:
        ouf.write("NO")
