expect = 0
probList = []
bList = []

with open("lottery.in") as inf:
    n, m = map(int, inf.readline().split())
    ai, bi = map(int, inf.readline().split())
    probList.append(1 / ai)
    bList.append(bi)
    for i in range(m - 1):
        ai, bi = map(int, inf.readline().split())
        probList.append(probList[i] / ai)
        bList.append(bi)
        expect += probList[i] * (1 - 1/ai) * bList[i]
    expect += probList[m - 1] * bList[m - 1]
with open("lottery.out", "w") as ouf:
    ouf.write(str(n - expect))

