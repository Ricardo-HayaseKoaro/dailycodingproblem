from collections import deque

def max_subarray(arr, k):
    for i in range(len(arr)):
        max = arr[i]
        if(i+k <= len(arr)):
            for aux_k in range(i, i + k):
                if arr[aux_k] > max:
                    max = arr[aux_k]
            print(max)
        else:
            return 0


def max_subarray2(arr, k):
    for i in range(len(arr) - k + 1):
        print(max(arr[i:i+k]))

def max_subarray_deque(arr, k):
    q = deque()
    for i in range(k):
        while q and arr[i] >= arr[q[-1]]: # pop off the values that are minor than the current value, q[-1] is the index of the last value that matters
            q.pop()
        q.append(i)

    for i in range(k, len(arr)):
        print(arr[q[0]])
        while q and q[0] <= i - k:
            q.popleft();
        while q and arr[i] >= arr[q[-1]]: # pop off the values that are minor than the current value, q[-1] is the index of the last value that matters
            q.pop()
        q.append(i)
    print(arr[q[0]])



array = [10, 5, 2, 7, 8, 7]
k = 3
max_subarray_deque(array, k)