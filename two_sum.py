def two_sum(nums, target):
    seen = {}  # Dictionary to store value: index
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices:", result)  # Output: [0, 1]
