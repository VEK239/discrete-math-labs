with open("problem1.in") as inf:
    word = inf.readline().split()[0]
    n, m, k = map(int, inf.readline().split())
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
            changesList[int(tmp[0])] = {tmp[2] : {int(tmp[1])}}
accepts = True
currPos = {1}
for i in range(len(word)):
    newCurrPos = set()
    if len(currPos) == 0:
        accepts = False
        break
    for pos in currPos:
        if pos in changesList and word[i] in changesList[pos]:
            newCurrPos = newCurrPos.union(changesList[pos][word[i]])
    currPos = newCurrPos
if len(currPos.intersection(determinedList)) == 0:
    accepts = False
with open("problem1.out", "w") as ouf:
    if accepts:
        ouf.write("Accepts")
    else:
        ouf.write("Rejects")