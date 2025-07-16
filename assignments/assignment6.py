# specila series
def special_series(n, m):
    total = 0
    power = 1
    sign = 1
    for i in range(1, 2*m, 2):
        total += sign * (n**power / i)
        sign *= -1
        power *= 2
    return round(total, 2)

print(special_series(2, 5))
