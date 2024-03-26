from sorting import quick_sort, insertion_sort, merge_sort


def main():
    arr = [9, 7, 5, 3, 1, 2, 4, 6, 8]
    low = 0
    high = len(arr) - 1
    value = 10
    quick = quick_sort.quick_sort(arr, low, high)
    print('Quick_sort: ', quick)
    insert = insertion_sort.insertion_sort(arr)
    print('Insertion_sort: ', insert)
    merge = merge_sort.merge_sort(arr)
    print('Merge_sort: ', merge)


main()
