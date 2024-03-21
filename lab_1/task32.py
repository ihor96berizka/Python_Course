# binary_search function
def binary_search(arr, value, low, high):
    if high < low:
        return False
    mid = (low + high) // 2
    if arr[mid] > value:
        return binary_search(arr, value, low, mid - 1)
    elif arr[mid] < value:
        return binary_search(arr, value, mid + 1, high)
    else:
        return True


# linear_search function
def linear_search(arr, value):
    i = 0
    while i < len(arr):
        if arr[i] == value:
            return True
        else:
            i += 1
    return False


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    value = 5
    low = 0
    high = len(arr) - 1
    result = binary_search(arr, value, low, high)
    print(result)
    result_2 = linear_search(arr, value)
    print(result_2)


main()
