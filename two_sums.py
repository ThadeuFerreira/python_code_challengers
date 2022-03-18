
def two_sum(arr, N):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == N:
                return True, i, j, arr[i], arr[j]
    return False, -1, -1, -1, -1

def two_sum_v2(arr, N):
    t_arr = sorted(arr)
    i = 0
    j = len(t_arr) - 1
    while i < j:
        if t_arr[i] + t_arr[j] == N:
            return True, t_arr[i], t_arr[j]
        elif t_arr[i] + t_arr[j] < N:
            i += 1
        else:
            j -= 1
    return False, -1, -1

arr = [1,9,25,25,2,3,4,5,6,7,8,9,10,30,15,42,8,25,25] 


print(two_sum(arr, 10))
print(two_sum_v2(arr, 10))
print(two_sum(arr, 50))
print(two_sum_v2(arr, 50))