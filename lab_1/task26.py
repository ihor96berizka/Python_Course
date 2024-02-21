def data_in():
    list_num = list(map(int, input("Enter a list of numbers: ").split()))
    return list_num


# insertion sort
def insertion_sort(list_num):
    for j in range(1, len(list_num)):
        key = list_num[j]
        i = j - 1
        while i >= 0 and list_num[i] > key:
            list_num[i + 1] = list_num[i]
            i = i - 1
        list_num[i + 1] = key
    return list_num


def main():
    num = data_in()
    print("Incoming data: ", num)
    result = insertion_sort(num)
    print("Sorted data: ", result)


main()
