import random 

def deterministic_select(arr, k):
    """
    Finds the k-th smallest element in the array using the Median of Medians algorithm.
    :param arr: List of elements
    :param k: Index (1-based) of the k-th smallest element
    :return: The k-th smallest element
    """
    if len(arr) == 1:
        return arr[0]
    
    def partition(arr, pivot):
        left, right, equal = [], [], []
        for x in arr:
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                equal.append(x)
        return left, equal, right
    
    def find_median(subarr):
        subarr.sort()
        return subarr[len(subarr) // 2]
    
    # Step 1: Divide the array into groups of 5 and find their medians
    medians = [find_median(arr[i:i + 5]) for i in range(0, len(arr), 5)]
    
    # Step 2: Recursively find the median of medians
    pivot = deterministic_select(medians, len(medians) // 2 + 1)
    
    # Step 3: Partition the array around the pivot
    left, equal, right = partition(arr, pivot)
    
    # Step 4: Determine which partition contains the k-th smallest element
    if k <= len(left):
        return deterministic_select(left, k)
    elif k <= len(left) + len(equal):
        return pivot
    else:
        return deterministic_select(right, k - len(left) - len(equal))

def randomized_select(arr, k):
    """
    Finds the k-th smallest element in the array using the Randomized Quickselect algorithm.
    :param arr: List of elements
    :param k: Index (1-based) of the k-th smallest element
    :return: The k-th smallest element
    """
    if len(arr) == 1:
        return arr[0]
    
    def partition(arr, pivot):
        left, right, equal = [], [], []
        for x in arr:
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                equal.append(x)
        return left, equal, right
    
    # Step 1: Choose a random pivot
    pivot = random.choice(arr)
    
    # Step 2: Partition the array around the pivot
    left, equal, right = partition(arr, pivot)
    
    # Step 3: Determine which partition contains the k-th smallest element
    if k <= len(left):
        return randomized_select(left, k)
    elif k <= len(left) + len(equal):
        return pivot
    else:
        return randomized_select(right, k - len(left) - len(equal))
if __name__ == "__main__":
    import time
    import numpy as np

    # Test data
    arr_sizes = [100, 1000, 10000]
    for size in arr_sizes:
        test_arr = np.random.randint(0, 10000, size).tolist()
        k = len(test_arr) // 2  # Median
        
        print(f"\nArray size: {size}, k = {k}")
        
        # Deterministic Select
        start_time = time.time()
        result_deterministic = deterministic_select(test_arr, k)
        print(f"Deterministic Select: {result_deterministic} (Time: {time.time() - start_time:.4f}s)")
        
        # Randomized Select
        start_time = time.time()
        result_randomized = randomized_select(test_arr, k)
        print(f"Randomized Select: {result_randomized} (Time: {time.time() - start_time:.4f}s)")
