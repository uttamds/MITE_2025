def is_valid(s):
    stack = []
    # Map closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():  # If it's an opening bracket
            stack.append(char)
        elif char in bracket_map:  # If it's a closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()  # Pop the matching opening bracket
        else:
            return False  # Invalid character (optional depending on constraints)

    return not stack  # True if stack is empty at the end

# Test cases
print(is_valid("()"))        # True
print(is_valid("()[]{}"))    # True
print(is_valid("(]"))        # False
print(is_valid("([)]"))      # False
print(is_valid("{[]}"))      # True
