from Quicksort import randomized_quicksort, deterministic_quicksort
import time
import numpy as np

# Testing with various cases
array_sizes = [100, 1000, 10000]
distributions = {
    "Random": lambda n: np.random.randint(0, 100, n),
    "Sorted": lambda n: np.arange(n),
    "Reverse": lambda n: np.arange(n, 0, -1),
    "Repeated": lambda n: np.random.choice([5, 10, 20], n)
}

for size in array_sizes:
    for desc, generator in distributions.items():
        test_arr = generator(size)
        arr_copy = test_arr.copy()

        # Time Randomized Quicksort
        start_time = time.time()
        randomized_quicksort(test_arr, 0, len(test_arr) - 1)
        rand_time = time.time() - start_time

        # Time Deterministic Quicksort
        start_time = time.time()
        deterministic_quicksort(arr_copy, 0, len(arr_copy) - 1)
        det_time = time.time() - start_time

        print(f"Size: {size}, {desc} Array - Randomized Quicksort: {rand_time:.5f}s, Deterministic Quicksort: {det_time:.5f}s")
