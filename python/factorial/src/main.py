def factorinal(n):
    if n == 0:
        return 1
    else:
        return n * factorinal(n - 1)
print(factorinal(5))
