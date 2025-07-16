def even_index_sum(n):
    s = str(n)
    return sum(int(s[i]) for i in range(len(s)) if i % 2 == 0)

print(even_index_sum(123456))  # Output: 9 (1+3+5)
