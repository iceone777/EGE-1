def f(n):
    if n <= 2025:
        return 1
    elif n < 2025:
        return n - f(n + 2) - f(n + 4)
result = f(20) + f(25)
print(result)