def CYK():
    n = len(word)
    partialResults = [[[0 for i in range(n)] for j in range(n)] for k in range(26)]
    for i in range(n):
        let = word[i]
        for tmp in terminalProductions:
            if tmp[1] == let:
                partialResults[tmp[0]][i][i] += 1
    for m in range(1, n):
        for i in range(n - m):
            j = i + m
            for k in range(i, j):
                for lst in interminalProductions:
                    partialResults[lst[0]][i][j] += partialResults[lst[1][0]][i][k] \
                                                              * partialResults[lst[1][1]][k + 1][j]
    return partialResults[ord(startSymbol) - 65][0][n - 1]


with open("nfc.in") as inf:
    productCount, startSymbol = inf.readline().split()
    productCount = int(productCount)
    terminalProductions = []
    interminalProductions = []
    for i in range(productCount):
        lst = inf.readline().split(' ->')
        a = lst[0]
        if len(lst) > 1:
            b = lst[1]
        else:
            b = ''
        b = b.replace('\n', '').replace(' ', '')
        if len(b) == 2:
            interminalProductions.append([ord(a) - 65, [ord(b[0]) - 65, ord(b[1]) - 65]])
        else:
            terminalProductions.append([ord(a) - 65, b])
    word = inf.readline().replace('\n', '').replace(' ', '')
    # print(backInterminalProductions)
with open("nfc.out", "w") as ouf:
    ouf.write(str(CYK() % 1000000007))
