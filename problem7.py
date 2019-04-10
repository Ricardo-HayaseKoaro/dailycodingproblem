"""
010 or 0 => n=0
'' => n = 1
1 = a => n =1
11 = aa + ak => n = 2
111 = aaa + ak +ka => n = 3
1111 = aaaa + aak + kaa + aka + kk => n = 5

decode !+ n_ways

12345 = a + decode(2345) or(+)  l + decode(345)

if array[:2] < 27
    result = n_ways[2:] + n_ways[1:]
else
    result = n+ways[1:]

PROBLEM with memory
when string = s0mething like 1111 will create a tree
n_ways(1) and n_ways(11) and n_ways(111) will be calculated more than one time
i will use a heap to save the n_ways
"""


def n_ways(array):
    if array.startswith('0'):
        return 0
    elif len(array) <= 1:
        return 1

    if int(array[:2]) < 27:
        result = n_ways(array[2:]) + n_ways(array[1:])
    else:
        result = n_ways(array[1:])
    return result


def helper(array, k, memo):
    if k <= 0:
        return 1
    s = len(array) - k
    if array[s] == '0':
        return 0

    if memo[k] is not None:
        return memo[k]

    result = helper(array, k-1, memo)
    if k>=2 and (int(array[:2])) <= 26:
        result += helper(array, k - 2, memo)
    memo[k] = result
    return result


def n_ways2(array):
    memo = [None] * (len(array)+1)
    return helper(array, len(array), memo)






