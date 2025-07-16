def odd_index_even_digits_sum(n):
    s = str(n)
    return sum(int(s[i]) for i in range(len(s)) if i % 2 == 1 and int(s[i]) % 2 == 0)

print(odd_index_even_digits_sum(123456))  # Output: 4
