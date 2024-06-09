def variables():
    print("starting")
    a = 3
    b = 5
    c = 7
    print(a, b, c)
    return a, b, c

def read(a, b, c):
    if a > c:
        print("a is the biggest")
    else:
        print("C is the biggest")
    if b > c:
        print("b is the biggest")
    else:
        print("c is the biggest")
        
    print("stopping")

a, b, c = variables()
read(a, b, c)

