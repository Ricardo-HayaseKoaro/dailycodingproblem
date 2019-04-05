
array = [1, 2, 3, 4, 5];
#my solution 
def my_solution(array):
  product = 1;
  for x in array:
    product = product*x;
  new = [];
  for x in array:
    new.append(product/x);
  print(new);


#solution without division
def solution_no_div(array):
  pre_prod = [];
  for x in array:
    if pre_prod:
      pre_prod.append(pre_prod[-1]*x); #get last value in array
    else:
      pre_prod.append(x); #first value
  
  pos_prod = [];
  for x in reversed(array):
    if pos_prod:
      pos_prod.append(pos_prod[-1]*x); #get last value in array
    else:
      pos_prod.append(x); #first value

  pos_prod = list(reversed(pos_prod));

  result = [];
  for i in range(len(array)):
    if i==0:
      result.append(pos_prod[i+1]);
    elif i == len(array) - 1: 
      result.append(pre_prod[i-1]);
    else:
      result.append(pos_prod[i+1]*pre_prod[i-1]);
  print(result);

my_solution(array)
solution_no_div(array)


  





  

