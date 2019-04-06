def my_solution(array):
    aux = set(array)
    missing = 1
    while missing in array:
        missing+=1
    return missing

def solution_space_const(array):
    if not array:
        return 1
    for i,whatever in enumerate(array):
        while i+1 != array[i] and 0 < array[i] <= len(array): #i+1 because i starts at 0, while index != array[index]
            aux = array[i]
            array[i], array[aux-1] = array[aux-1], array[i] #swap values
            if(array[i] == array[aux-1]):
                break
    for i,num in enumerate(array,1):
        if num != i:
            return i
    return len(array)+1

array = [3, 4, -1, 1]
array2 = [1, 2, 0]
print(solution_space_const(array))
