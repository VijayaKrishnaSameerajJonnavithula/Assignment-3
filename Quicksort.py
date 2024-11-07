import random
import numpy as np

# Randomized Quicksort Implementation
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

# Deterministic Quicksort Implementation with Median-of-Three Pivot
def deterministic_partition(arr, low, high):
    mid = (low + high) // 2
    pivot_candidates = [arr[low], arr[mid], arr[high]]
    pivot_candidates.sort()
    pivot_value = pivot_candidates[1]

    # Use np.where() to find the index of the pivot in the array
    pivot_index = np.where(arr[low:high + 1] == pivot_value)[0][0] + low  # Adjust for slicing

    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quicksort(arr, low, high):
    while low < high:
        pivot_index = deterministic_partition(arr, low, high)
        # Recursively sort the smaller part to minimize stack depth
        if pivot_index - low < high - pivot_index:
            deterministic_quicksort(arr, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            deterministic_quicksort(arr, pivot_index + 1, high)
            high = pivot_index - 1
