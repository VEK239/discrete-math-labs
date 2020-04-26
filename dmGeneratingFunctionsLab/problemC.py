def print_polynomial(P):
    deg = len(P) - 1
    while P[deg] == 0:
        deg -= 1
    P = P[:deg + 1]
    print(len(P) - 1)
    print_list(P)


print_list = lambda l: print(' '.join(map(lambda x: str(x), l)))
get_value = lambda l, x: l[x] if x < len(l) else 0
f = lambda x: sum([coefs[i] * get_value(elements, x - i - 1) for i in range(x)])

if __name__ == "__main__":
    k = int(input())
    elements = list(map(int, input().split()))
    coefs = list(map(int, input().split()))
    Q = [1] + [-coefs[i] for i in range(k)]
    P = [elements[0]] + [elements[i] - f(i) for i in range(1, k)]
    print_polynomial(P)
    print_polynomial(Q)
