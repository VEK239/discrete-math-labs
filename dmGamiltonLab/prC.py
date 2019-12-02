from functools import cmp_to_key

def comp(a, b):
    print(1, a, b)
    if (input().split()[0] == "YES"):
        return -1
    else:
        return 1


n = int(input())
lamps = [i + 1 for i in range(n)]
lamps = sorted(lamps, key=cmp_to_key(comp))
print(0, end=' ')
for lamp in lamps:
    print(lamp, end=' ')