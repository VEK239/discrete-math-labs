with open("automaton.in") as inf:
    productCount, startSymbol = inf.readline().split()
    productCount = int(productCount)
    productions = {}
    for i in range(productCount):
        a, b = inf.readline().split(' -> ')
        if a in productions:
            productions[a].add(b.replace('\n', ''))
        else:
            productions[a] = {b.replace('\n', '')}
    wordsCount = int(inf.readline())
    st = ''
    for i in range(wordsCount):
        correctWord = False
        word = inf.readline().replace('\n', '')
        length = 0
        curPos = {startSymbol}
        for letter in word:
            foundLetter = False
            # print(curPos)
            newPos = set()
            goingPos = set()
            for going in curPos:
                if going in productions:
                    newPos = newPos.union(productions[going])
            for pr in newPos:
                if pr[0] == letter:
                    foundLetter = True
                    if len(pr) == 1:
                        if length + 1 == len(word):
                            correctWord = True
                            break
                    else:
                        goingPos.add(pr[1])
            if foundLetter:
                length += 1
            curPos = goingPos
        if correctWord:
            st += 'yes\n'
        else:
            st += 'no\n'
with open("automaton.out", "w") as ouf:
    ouf.write(st)