with open("problem1.in") as inf:
    word = inf.readline().split()[0]
    n, m, k = map(int, inf.readline().split())
    determinedList = list(map(int, inf.readline().split()))
    changesList = {}
    for i in range(m):
        tmp = inf.readline().split()
        if int(tmp[0]) in changesList:
            changesList[int(tmp[0])][tmp[2]] = int(tmp[1])
        else:
            changesList[int(tmp[0])] = {tmp[2] : int(tmp[1])}
accepts = True
currPos = 1
for i in range(len(word)):
    if currPos in changesList and word[i] in changesList[currPos]:
        currPos = changesList[currPos][word[i]]
    else:
        accepts = False
        print(word[i])
        break
if currPos not in determinedList:
    accepts = False
with open("problem1.out", "w") as ouf:
    if accepts:
        ouf.write("Accepts")
    else:
        ouf.write("Rejects")