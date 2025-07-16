def hemachandra(n):
    if n == 1: return 1
    if n == 2: return 2
    return hemachandra(n-1) + hemachandra(n-2)

print(hemachandra(6))  # Output: 18
