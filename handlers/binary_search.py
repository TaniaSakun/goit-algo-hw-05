def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iter_count = 0

    while low < high:
        mid = (high + low) // 2
        iter_count += 1

        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid

    upper_bound = arr[low] if low < len(arr) and arr[low] >= x else None

    return iter_count, upper_bound
