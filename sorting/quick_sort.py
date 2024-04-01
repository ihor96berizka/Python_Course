import random


def partition(arr, low, high):
    pivot = low
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return pivot


def random_partition(arr, low, high):
    randpivot = random.randrange(low, high)
    arr[low], arr[randpivot] = arr[randpivot], arr[low]
    return partition(arr, low, high)


def random_quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        q = random_partition(arr, low, high)

        random_quick_sort(arr, low, q - 1)
        random_quick_sort(arr, q + 1, high)

    return arr
