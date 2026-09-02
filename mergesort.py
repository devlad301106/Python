def merge(a, low, mid, high):
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1]

    i = 0
    j = 0

    print("M(a," + str(low + 1) + "," + str(mid + 1) + "," + str(high + 1) + ")")

    for k in range(low, high + 1):

        if j >= len(right) or (i < len(left) and left[i] <= right[j]):
            a[k] = left[i]
            i += 1

        else:
            a[k] = right[j]
            j += 1


def mergeSort(a, low, high):
    mid = (low + high) // 2

    print("MS(a," + str(low + 1) + "," + str(high + 1) + ")")

    if low >= high:
        return

    mergeSort(a, low, mid)
    mergeSort(a, mid + 1, high)
    merge(a, low, mid, high)


a = [7, 5, 4, 9]

mergeSort(a, 0, len(a) - 1)

for num in a:
    print(num, end=" ")