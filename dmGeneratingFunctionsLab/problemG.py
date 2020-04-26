def generate_string(s):
    for i in s:
        if i not in ['(', ')', ',']:
            yield i


def coef(n, k):
    ans = 1
    for i in range(k):
        ans *= ((n - k + i + 1) / (i + 1))
    return ans


def parse():
    char = next(sequence)
    if char == 'B':
        return [0, 1, 0, 0, 0, 0, 0]
    elif char == 'L':
        element = parse()
        weights = [1]
        for i in range(1, 7):
            weights.append(sum(element[j] * weights[i - j] for j in range(1, i + 1)))
        return weights
    elif char == 'P':
        left = parse()
        right = parse()
        return [sum(left[j] * right[i - j] for j in range(i + 1)) for i in range(7)]
    elif char == 'S':
        element = parse()
        subweights = [[1 for _ in range(7)]] + [[0 for _ in range(7)] for _ in range(6)]
        weights = [1]
        for i in range(1, 7):
            for j in range(1, 7):
                subweights[i][j] = sum(coef(element[j] + k - 1, k) * subweights[i - k * j][j - 1] for k in range(i // j + 1))
            weights.append(subweights[i][i])
        return weights


if __name__ == "__main__":
    sequence = generate_string(input().strip())
    print(' '.join(map(lambda x: str(int(x)), parse())))
