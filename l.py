def mult(t):
    r = 1
    for i in t:
        r *= i
    return r

# Example usage
i = (1, 2, 3, 4, 5)
p = mult(i)
print(i)
print(f"Product of all the numbers: {p}")
