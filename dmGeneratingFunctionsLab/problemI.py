MOD = 104857601
if __name__ == "__main__":
    k, n = map(int, input().split())
    n -= 1
    elements = list(map(int, input().split())) + [0 for i in range(k)]
    coefs = [1] + list(map(lambda x: -int(x) % MOD, input().split()))
    while n >= k:
        for i in range(k, 2 * k):
            elements[i] = 0
            for j in range(k):
                elements[i] = (elements[i] - coefs[j + 1] * elements[i - j - 1] % MOD) % MOD
        elements = [elements[i] for i in range(n % 2, 2 * k, 2)] + [0 for i in range(k)]

        new_coefs = [0 for i in range(k + 1)]
        for i in range(0, 2 * k + 1, 2):
            for j in range(i + 1):
                q_left = coefs[j] if j <= k else 0
                q_right = (coefs[i - j] * (-1 if ((i - j) % 2 == 1) else 1) if i - j <= k else 0)
                new_coefs[i >> 1] = (new_coefs[i >> 1] + q_left * q_right % MOD) % MOD
        coefs = new_coefs
        n >>= 1
    print(elements[n] % MOD)
