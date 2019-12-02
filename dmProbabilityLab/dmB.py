prob = 0
with open("shooter.in") as inf:
    n, m, k = map(int, inf.readline().split())
    prob = list(map(float, inf.readline().split()))
sumProb = 0
for i in range(len(prob)):
    tmp = 1 - prob[i]
    prob[i] = 1
    for j in range(m):
        prob[i] *= tmp
    prob[i] = prob[i]
    sumProb += prob[i]
with open("shooter.out", "w") as ouf:
    ouf.write(str(prob[k - 1] / sumProb))


