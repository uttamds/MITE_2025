def remove_element(nums, val):
    k = 0  # Count of elements not equal to val

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

# Example usage:
nums = [3, 2, 2, 3]
val = 3
length = remove_element(nums, val)
print("New length:", length)
print("Modified array:", nums[:length])  # Only the first `length` elements are valid
