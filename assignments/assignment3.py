def count_prime_digits(n):
    return sum(1 for d in str(n) if int(d) in {2, 3, 5, 7})

print(count_prime_digits(2375418))  # Output: 4
