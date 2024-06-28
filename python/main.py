# Fizz buzz

for f in range(1, 101):
    if f % 3 == 0 and f % 5 == 0:
        print(f'{f}: FizzBuzz')
    if f % 3 == 0:
        print(f'{f}: Fizz')
    if f % 5 == 0:
        print(f'{f}: Buzz')
    else:
        print(f'{f}: Nor fizz or buzz or fizzbuzz')