print_list = lambda l: print(' '.join(map(lambda x: str(x), l)))
get_value = lambda l, x: l[x] if x < len(l) else 0
f = lambda x: sum([coefs[i] * get_value(elements, x - i - 1) for i in range(x)])


def print_polynomial(P):
    deg = len(P) - 1
    while P[deg] == 0:
        deg -= 1
    P = P[:deg + 1]
    print(len(P) - 1)
    print_list(P)


def multiply(left, right):
    cur = [0 for _ in range(len(left) + 1)]
    for i, l in enumerate(left):
        for j, r in enumerate(right):
            if l * r != 0:
                cur[i + j] += l * r
    return cur


if __name__ == "__main__":
    r = int(input())
    d = int(input())
    polynomial = list(map(int, input().split()))
    factor = [1, -r]
    Q = factor
    for i in range(d):
        Q = multiply(Q, factor)
    coefs = [-q for q in Q][1:]
    elements = [sum(coef * (e ** deg) * (r ** e) for deg, coef in enumerate(polynomial)) for e in range(d + 1)]
    P = [elements[0]] + [elements[i] - f(i) for i in range(1, d + 1)]
    print_polynomial(P)
    print_polynomial(Q)
