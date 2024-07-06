# Exercise: Filter and Map
#
# Write a function that takes a list of numbers and does the following:
#
# 1. Filters out all even numbers.
# 2. Doubles each remaining number.
# 3. Returns the modified list.
#
# For example, given the list [1, 2, 3, 4, 5], the function should return [2, 6, 10].
def filter0(begin, end):
    numbers = []
    for i in range(begin,end):
        if i % 2 != 0:
            numbers.append(i * 2)
    return numbers
print(filter0(1, 6))

# I was close for this problem.