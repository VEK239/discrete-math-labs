from fractions import Fraction
from math import factorial


def multiply(left, right):
    cur = [0 for _ in range(len(left))]
    for i, l in enumerate(left):
        for j, r in enumerate(right):
            if l * r != 0:
                cur[i + j] += l * r
    return cur


def p(k, start):
    polynomials = [[i, 1] + [0 for _ in range(k - 2)] for i in range(start, start + k - 1)]
    cur_polynomial = polynomials[0]
    for i in range(1, len(polynomials)):
        cur_polynomial = multiply(cur_polynomial, polynomials[i])
    return cur_polynomial


if __name__ == "__main__":
    r, k = map(int, input().split())
    k += 1
    coefs = list(map(int, input().split()))
    fact = factorial(k - 1)
    polynomial_coefs = [0 for _ in range(k)]
    for deg, coef in enumerate(coefs):
        cur_polynomial = [Fraction(i * coef, r ** deg) for i in p(k, -deg + 1)]
        for i, c in enumerate(cur_polynomial):
            polynomial_coefs[i] += c
    for i in range(len(polynomial_coefs)):
        polynomial_coefs[i] /= fact
    print(' '.join(map(lambda x: str(x.numerator) + '/' + str(x.denominator), polynomial_coefs)))
