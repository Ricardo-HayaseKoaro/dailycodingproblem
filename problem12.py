
def n_ways_climb(n, steps):
    result = 0
    if n == 0:
        return 1
    if n < 0:
        return 0
    for x in steps:
        result += n_ways_climb(n-x, steps)
    return result


def n_ways_climb2(n, steps, memo):
    result = 0
    if n == 0:
        return 1
    if n < 0:
        return 0
    if memo[n] is None:
        for x in steps:
            result += n_ways_climb2(n - x, steps, memo)
            memo[n] = result
        return memo[n]
    else:
        return memo[n]


def how_climb(n, steps, map):
    if n == 0:
        print(map)
        return 0
    if n < 0:
        return 0
    for x in steps:
        aux_map = map.copy()
        aux_map.append(x)
        how_climb(n - x, steps, aux_map)
    return 0




steps = [1, 2]
map = []
memo = [None]*5
print(n_ways_climb2(4, steps, memo))
how_climb(4, steps, map)

