def binary_search(arr, target, low, high):
    
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

l = [1, 2, 4, 5, 6, 7]
target = 6
low = 0
high = len(l)

print(binary_search(l, target, low, high))