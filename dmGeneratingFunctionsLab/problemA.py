print_list = lambda l: print(' '.join(map(lambda x: str(x % 998244353), l)))
get_value = lambda l, x: l[x] if x < len(l) else 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    print(max(m, n))
    print_list([(get_value(p, i) + get_value(q, i)) for i in range(max(m, n) + 1)])

    print(m + n)
    mult_function = [0 for i in range(m + n + 1)]
    for i in range(n + m + 1):
        for j in range(min(i, m) + 1):
            mult_function[i] += get_value(p, i - j) * get_value(q, j)
    print_list(mult_function)

    div_function = [get_value(p, i) for i in range(1000)]
    for i in range(1000):
        for j in range(1, min(i, m) + 1):
            div_function[i] -= div_function[i - j] * get_value(q, j)
    print_list(div_function)
