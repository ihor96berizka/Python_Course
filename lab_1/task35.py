from sorting import quick_sort, insertion_sort, merge_sort
import matplotlib.pyplot as plt
import random
import datetime


def generate_random_list(size):
    return [random.randint(1, 1000000) for _ in range(size)]


def main():
    initial_list_size = 1000
    size_step = 10
    max_list_size = 1000000
    current_size = initial_list_size

    list_sizes_merge_sort = []
    execution_time_merge_sort = []

    list_sizes_insertion_sort = []
    execution_time_insertion_sort = []

    list_sizes_quick_sort = []
    execution_time_quick_sort = []

    while current_size <= max_list_size:
        original_list = generate_random_list(current_size)

        list_to_be_sorted_1 = original_list[:]
        start_time = datetime.datetime.now()
        merge_sort.merge_sort(list_to_be_sorted_1)
        end_time = datetime.datetime.now()
        list_sizes_merge_sort.append(current_size)
        execution_time_merge_sort.append(end_time - start_time)

        list_to_be_sorted_2 = original_list[:]
        start_time = datetime.datetime.now()
        insertion_sort.insertion_sort(list_to_be_sorted_2)
        end_time = datetime.datetime.now()
        list_sizes_insertion_sort.append(current_size)
        execution_time_insertion_sort.append(end_time - start_time)

        list_to_be_sorted_3 = original_list[:]
        low = 0
        high = len(list_to_be_sorted_3) - 1
        start_time = datetime.datetime.now()
        quick_sort.random_quick_sort(list_to_be_sorted_3, low, high)
        end_time = datetime.datetime.now()
        list_sizes_quick_sort.append(current_size)
        execution_time_quick_sort.append(end_time - start_time)

        print(current_size)
        current_size = current_size * size_step

    execution_time_quick_sort_seconds = [time.total_seconds() for time in execution_time_quick_sort]
    execution_time_insertion_sort_seconds = [time.total_seconds() for time in execution_time_insertion_sort]
    execution_time_merge_sort_seconds = [time.total_seconds() for time in execution_time_merge_sort]

    plt.plot(list_sizes_quick_sort, execution_time_quick_sort_seconds, label='Quick Sort', color='green')
    plt.plot(list_sizes_insertion_sort, execution_time_insertion_sort_seconds, label='Insertion Sort', color='blue')
    plt.plot(list_sizes_merge_sort, execution_time_merge_sort_seconds, label='Merge Sort', color='red')

    plt.xlabel('Розмір ліста')
    plt.ylabel('Час виконання (с)')
    plt.title('Порівняння часу виконання алгоритмів сортування')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
