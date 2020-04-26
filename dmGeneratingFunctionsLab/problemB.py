MOD = 998244353
print_list = lambda l: print(' '.join(map(lambda x: str(x % MOD), l)))
get_value = lambda l, x: l[x] if x < len(l) else 0


def gcd(a, b):
    if a == 0:
        return b, 0, 1
    d, x1, y1 = gcd(b % a, a)
    x = y1 - b // a * x1
    y = x1
    return d, x, y


def get_reverse(a):
    g, x, y = gcd(a, MOD)
    return 1 if g != 1 else (x % MOD + MOD) % MOD


def multiply(p, q):
    mult_function = [0 for i in range(101)]
    for i in range(101):
        for j in range(i + 1):
            mult_function[i] += get_value(p, i - j) * get_value(q, j)
    return mult_function


def get_sum(function_coefs):
    answer = [0 for i in range(m)]
    for i in range(m):
        for j in range(m):
            answer[i] += function_coefs[j] * p_deg_coefs[j][i] % MOD
    print_list(answer)


if __name__ == "__main__":
    n, m = map(int, input().split())
    p = list(map(int, input().split())) + [0 for i in range(99)]

    p_deg_coefs = [[1] + [0 for i in range(100)], p]
    for i in range(99):
        p_deg_coefs.append(multiply(p_deg_coefs[-1], p))

    exp_coefs = [1] + [0 for i in range(m)]
    for i in range(1, m):
        exp_coefs[i] = get_reverse(i) * exp_coefs[i - 1] % MOD
    # print(exp_coefs)

    ln_coefs = [0, 1] + [0 for i in range(m - 1)]
    for i in range(2, m):
        ln_coefs[i] = get_reverse(i) * (1 - i) * ln_coefs[i - 1] % MOD
    # print(ln_coefs)

    sqrt_coefs = [1] + [0 for i in range(m)]
    for i in range(1, m):
        sqrt_coefs[i] = get_reverse(2 * i) * (3 - 2 * i) * sqrt_coefs[i - 1] % MOD
    # print(sqrt_coefs)

    get_sum(sqrt_coefs)
    get_sum(exp_coefs)
    get_sum(ln_coefs)
