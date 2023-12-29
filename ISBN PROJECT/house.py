import random
import time

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])
    return merge(arr1, arr2)

def merge(arr1, arr2):
    arr = []
    i = j = k = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
        k += 1

    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
        k += 1

    while j < len(arr2):
        arr.append(arr2[j])
        j += 1
        k += 1

    return arr

def main():
    size = 500
    arr = [random.randint(0, 999) for _ in range(size)]

    print("Unsorted Array:")
    print(arr)

    # Quick Sort
    quick_sort_arr = arr.copy()
    start_time = time.time()
    quick_sort(quick_sort_arr, 0, size - 1)
    end_time = time.time()
    time_taken_quick_sort = end_time - start_time

    print("\nSorted Array (Quick Sort):")
    print(quick_sort_arr)
    print(f"\nTime taken for Quick Sort: {time_taken_quick_sort:.6f} seconds")

    # Merge Sort
    merge_sort_arr = arr.copy()
    start_time = time.time()
    merge_sort_arr = merge_sort(merge_sort_arr)
    end_time = time.time()
    time_taken_merge_sort = end_time - start_time

    print("\nSorted Array (Merge Sort):")
    print(merge_sort_arr)
    print("\nTime taken for Merge Sort: {:.6f} seconds".format(time_taken_merge_sort))


main()
