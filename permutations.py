def permute(nums):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path)
            return
        for i in range(len(remaining)):
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
    
    backtrack([], nums)
    return result

# Example usage:
nums = [1, 2, 3]
print(permute(nums))

'''
Start: path=[], remaining=[1,2]

→ Choose 1 → path=[1], remaining=[2]
  → Choose 2 → path=[1,2], remaining=[] → ✅ add [1,2] to result

→ Backtrack

→ Choose 2 → path=[2], remaining=[1]
  → Choose 1 → path=[2,1], remaining=[] → ✅ add [2,1] to result
'''
