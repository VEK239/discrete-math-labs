import copy

with open("markchain.in") as inf:
    n = int(inf.readline())
    lst = []
    for i in range(n):
        lst.append(list(map(float, inf.readline().split())))

boo = True

while boo:
    newLst = copy.deepcopy(lst)
    boo = False
    for i in range(n):
        for j in range(n):
            newLst[i][j] = 0
            for k in range(n):
                newLst[i][j] += lst[i][k] * lst[k][j]
            if i != 0:
                if lst[i - 1][j] - lst[i][j] > 10e-10:
                    boo = True
    lst = newLst

with open("markchain.out", "w") as ouf:
    st = ''
    for i in range(n):
        num = 0
        for j in range(n):
            num += lst[j][i]
        st += str(num / n) + '\n'
    ouf.write(st)
