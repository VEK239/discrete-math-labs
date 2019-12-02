def dfs(u, v):
    visitedList[u - 1] = True
    if (u in firstDeterminedList) ^ (v in secondDeterminedList):
        return False
    result = True
    if u in firstChangesList:
        for letter in firstChangesList[u]:
            if letter not in secondChangesList[v]:
                return False
            t1 = firstChangesList[u][letter]
            t2 = secondChangesList[v][letter]
            if (u == t1) ^ (v == t2):
                return False
            if not visitedList[t1 - 1]:
                result = result and dfs(t1, t2)
    else:
        if v in secondChangesList:
            return False
    return result


with open("isomorphism.in") as inf:
    n, m, k = map(int, inf.readline().split())
    firstDeterminedList = set(map(int, inf.readline().split()))
    firstChangesList = {}
    for i in range(m):
        tmp = inf.readline().split()
        if int(tmp[0]) in firstChangesList:
            firstChangesList[int(tmp[0])][tmp[2]] = int(tmp[1])
        else:
            firstChangesList[int(tmp[0])] = {tmp[2]: int(tmp[1])}
    visitedList = [False for i in range(n)]
    n, m, k = map(int, inf.readline().split())
    secondDeterminedList = set(map(int, inf.readline().split()))
    secondChangesList = {}
    for i in range(m):
        tmp = inf.readline().split()
        if int(tmp[0]) in secondChangesList:
            secondChangesList[int(tmp[0])][tmp[2]] = int(tmp[1])
        else:
            secondChangesList[int(tmp[0])] = {tmp[2]: int(tmp[1])}

with open("isomorphism.out", "w") as ouf:
    if dfs(1, 1):
        ouf.write("YES")
    else:
        ouf.write("NO")
