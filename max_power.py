def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

def findMaxValueInArrayTowArrays(arr1, arr2):
    return max(arr1 + arr2)

def knapsack(arr, capacity):
    if len(arr) == 0 or capacity == 0:
        return 0
    if arr[0] > capacity:
        return knapsack(arr[1:], capacity)
    return max(arr[0] + knapsack(arr[1:], capacity - arr[0]), knapsack(arr[1:], capacity))

print(quicksort([1,2,3,4,5,6,7]))
print(quicksort([7,6,5,4,30,3,2,1]))
    
