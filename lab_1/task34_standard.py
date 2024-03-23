def partition(arr, low, high):
    # index of low element
    i = low - 1
    # pivot(root)
    pivot = arr[high]

    for j in range(low, high):
        # If the current element is less than or equal to pivot
        if arr[j] <= pivot:
            # increase the index of the smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        q = partition(arr, low, high)

        quick_sort(arr, low, q - 1)
        quick_sort(arr, q + 1, high)


def main():
    arr = [9, 7, 5, 3, 1, 2, 4, 6, 8]
    low = 0
    high = len(arr) - 1
    quick_sort(arr, low, high)
    print(arr)


main()
