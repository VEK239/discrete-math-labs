print_list = lambda l: print(' '.join(map(lambda x: str(x % 1000000007), l)))

if __name__ == "__main__":
    weights_count, max_weight = map(int, input().split())
    weights = list(map(int, input().split()))
    trees = [1] + [0 for i in range(max_weight)]
    subtrees = [1] + [0 for i in range(max_weight)]
    for j in range(max_weight):
        trees[j + 1] = sum(subtrees[j + 1 - i] for i in weights if i <= j + 1) % 1000000007
        subtrees[j + 1] = sum(trees[j + 1 - i] * trees[i] % 1000000007 for i in range(j + 2)) % 1000000007
    print_list(trees[1:])
