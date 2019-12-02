st = set()
with open("useless.in") as inf:
    productCount, startSymbol = inf.readline().split()
    st.add(startSymbol)
    productCount = int(productCount)
    productions = {}
    for i in range(productCount):
        lst = inf.readline().split(' ->')
        a = lst[0]
        if len(lst) > 1:
            b = lst[1]
        else:
            b = ''
        st.add(a)
        b = b.replace('\n', '').replace(' ', '')
        for let in b:
            if let.isupper():
                st.add(let)
        if a in productions:
            productions[a].add(b)
        else:
            productions[a] = {b}
# удалим непорождающие правила
usefulProductions = set()
for production in productions:
    for go in productions[production]:
        if go.lower() == go:
            usefulProductions.add(production)
differentSets = True
while differentSets:
    newUsefulProductions = {i for i in usefulProductions}
    for production in productions:
        for going in productions[production]:
            adding = True
            if going != '':
                for let in going:
                    if not let.islower() and not let in usefulProductions:
                        adding = False
                if adding:
                    newUsefulProductions.add(production)
                    break
    if len(newUsefulProductions) == len(usefulProductions):
        differentSets = False
    else:
        usefulProductions = newUsefulProductions
usefulBirthing = usefulProductions.copy()
print(usefulBirthing)

# changing productions
newProductions = {}
for production in productions:
    if production in usefulBirthing:
        newProductions[production] = set()
        for going in productions[production]:
            adding = True
            for let in going:
                if let.isupper() and let not in usefulBirthing:
                    adding = False
            if adding:
                newProductions[production].add(going)
productions = newProductions.copy()

# delete the ones we can't get to
usefulProductions = {startSymbol}
differentSets = True
while differentSets:
    newUsefulProductions = {i for i in usefulProductions}
    for production in productions:
        if production in newUsefulProductions:
            for el in productions[production]:
                for let in el:
                    if let.isupper():
                        newUsefulProductions.add(let)
    if len(newUsefulProductions) == len(usefulProductions):
        differentSets = False
    else:
        usefulProductions = newUsefulProductions
reachableProductions = usefulProductions.copy()

usefulProductions = reachableProductions.intersection(usefulBirthing)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
printing = ''
for let in alphabet:
    if let in st and let not in usefulProductions:
        printing += let + ' '
with open("useless.out", "w") as ouf:
    ouf.write(printing)