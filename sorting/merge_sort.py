def merge_sort(arr):
    if len(arr) > 1:
        # Знаходимо середину масиву
        mid = len(arr) // 2

        # Розділяємо масив на два підмасиви
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Рекурсивно сортуємо кожен підмасив
        merge_sort(left_half)
        merge_sort(right_half)

        # Злиття відсортованих підмасивів
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Перенесення залишкових елементів, якщо такі є
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr
