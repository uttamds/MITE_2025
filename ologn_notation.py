def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Demo
nums = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
result = binary_search(nums, target)

print("Target found at index:" if result != -1 else "Target not found", result)
