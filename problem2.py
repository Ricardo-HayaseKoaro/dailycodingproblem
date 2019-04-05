"""


"""


def my_solution(array, k):
  aux = {};
  for x in array:
    if(k - x) in aux:
      return True
    else:
     aux[x] = True
  return False;



array = [10, 15, 3, 7];
k = 17;

print(my_solution(array,k))