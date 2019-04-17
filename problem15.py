import random


def reservoir_sampling(big_f_array):
    result = None
    for i, aux in enumerate(big_f_array):
        if random.randint(1, i+1) == 1:
            result = aux
    return result


# this is a reservoir sampling if i forget rewatch https://www.youtube.com/watch?v=A1iwzSew5QY

