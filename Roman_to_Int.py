def roman_to_int(s):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0

    for char in reversed(s):  # Process from right to left
        current = roman_map[char]
        if current < prev_value:
            total -= current  # Subtract if smaller value before larger
        else:
            total += current
        prev_value = current
    
    return total

# Example usage:
print(roman_to_int("MCMXCIV"))  # Output: 1994
