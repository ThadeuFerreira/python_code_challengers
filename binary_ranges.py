def binary_search(arr, N, start, end):
    if start >= end:
        return False
    mid = (end - start)//2
    if N < arr[mid][0]:
        return binary_search(arr, N, start, mid-1)
    if N > arr[mid][1]:
        return binary_search(arr, N, mid+1, end)
    return N > arr[mid][0] or N < arr[mid][1]
    
def is_in_range_v2(arr, N):
    mid = len(arr)//2
    if N < arr[mid][0]:
        return binary_search(arr, N, 0, mid)
    if N > arr[mid][1]:
        return binary_search(arr, N, mid, len(arr) -1)
    return N > arr[mid][0] or N < arr[mid][1]
    
def is_in_range_v1(arr, N):
    for i in arr:
        if N >= i[0] and N <= i[1]:
            return True
    return False

arr = [(0,15), (32,63)]

N = 12

print(is_in_range_v2(arr,17))
print(is_in_range_v2(arr,N))
print(is_in_range_v2(arr,17))
