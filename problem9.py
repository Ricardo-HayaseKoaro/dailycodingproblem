# 0(2^n) im time
def largest_sum(array):
    if not array:
        return 0
    result1 = largest_sum(array[1:])
    result2 = array[0] + largest_sum(array[2:])
    return max(result1, result2)


# 0(n) in time
def largest_sum_2(array, memo):
    k = len(array)
    if not array:
        return 0
    if memo[k] is None:
        result1 = largest_sum_2(array[1:], memo)
        result2 = array[0] + largest_sum_2(array[2:], memo)
        return max(result1, result2)
    else:
        return memo[k]


array = [2, 4, 6, 2, 5]
memo = [None]*10000
print(largest_sum_2(array, memo))