def userinput():
    n = int(input("What number:  "))
    solution = factorinal(n)
    print(f"the factoral of {n} is: {solution}")
def factorinal(n):
    if n == 0:
        return 1
    else:
        return n * factorinal(n - 1)
userinput()