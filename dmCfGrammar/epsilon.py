with open("epsilon.in") as inf:
    productCount, startSymbol = inf.readline().split()
    productCount = int(productCount)
    productions = {}
    for i in range(productCount):
        lst = inf.readline().split(' ->')
        a = lst[0]
        if len(lst) > 1:
            b = lst[1]
        else:
            b = ''
        if a in productions:
            productions[a].add(b.replace('\n', '').replace(' ', ''))
        else:
            productions[a] = {b.replace('\n', '').replace(' ', '')}

epsilonProductions = set()
for production in productions:
    for go in productions[production]:
        if go == '':
            epsilonProductions.add(production)

differentSets = True
while differentSets:
    newEpsilonProductions = {i for i in epsilonProductions}
    for production in productions:
        result = productions[production]
        for going in result:
            includes = True
            for let in going:
                if let not in epsilonProductions:
                    includes = False
            if includes:
                newEpsilonProductions.add(production)
                break
    if len(newEpsilonProductions) == len(epsilonProductions):
        differentSets = False
    else:
        epsilonProductions = newEpsilonProductions

printing = ''
st = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for let in st:
    if let in epsilonProductions:
        printing += let + ' '

with open("epsilon.out", "w") as ouf:
    ouf.write(printing)