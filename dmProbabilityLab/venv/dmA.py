prob = 0
with open("exam.in") as inf:
    tCount, sCount = map(int, inf.readline().split())
    for i in range(tCount):
        stChecked, passProb = map(int, inf.readline().split())
        prob += (stChecked / sCount) * (passProb / 100)

with open("exam.out", "w") as ouf:
    ouf.write(str(prob))
