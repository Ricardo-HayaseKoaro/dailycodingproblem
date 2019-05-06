from math import inf

def min_cost(m):
    n = len(m)
    k = len(m[0])
    aux_solution = [0] * k
    for i, row in enumerate(m):
        aux_row = []
        for j, house_cost in enumerate(row):
            min_cost = min(aux_solution[x][j] for x in range(k) if x != j) + house_cost
            aux_row.append(min_cost)
        aux_solution = aux_row
    print(min(aux_solution[-1]))


def min_cost2(m):
    n = len(m)
    k = len(m[0])
    lowest_cost = 0
    lowest_cost_index = -1
    second_lowest_cost = 0
    for i, row in enumerate(m):
        new_lowest_cost, new_lowest_cost_index = inf, -1
        new_second_lowest_cost = inf
        for j, house_cost in enumerate(row):
            if j == lowest_cost_index:
                cost = second_lowest_cost + house_cost
            else:
                cost = lowest_cost + house_cost
            if cost < new_lowest_cost:
                new_second_lowest_cost = new_lowest_cost
                new_lowest_cost = cost
                new_lowest_cost_index = j
            elif cost < new_second_lowest_cost:
                new_second_lowest_cost = cost
        lowest_cost = new_lowest_cost
        lowest_cost_index = new_lowest_cost_index
        second_lowest_cost = new_second_lowest_cost
    print(lowest_cost)
