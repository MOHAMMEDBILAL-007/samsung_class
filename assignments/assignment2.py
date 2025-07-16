def second_smallest_digit(n):
    digits = sorted(set(map(int, str(n))))
    return digits[1] if len(digits) >= 2 else -1

print(second_smallest_digit(846873))  # Output: 4
