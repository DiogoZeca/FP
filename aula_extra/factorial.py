def factorial(n):
    assert isinstance(n, int)
    assert n >= 0
    if n == 0:  # base case
        return 1
    else:
        for i in range(1, n):
            n *= i
        return n

print(factorial(5))