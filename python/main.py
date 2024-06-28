# Fizz buzz
for i in range(1, 100):
    if i % 5 == 0 and i % 3 == 0:
        print(f'{i}: Fizzbuzz')
    elif i % 5 == 0:
        print(f'{i}: Fizz')
    elif i % 3 == 0:
        print(f'{i} Buzz')
    else:
        print(i)