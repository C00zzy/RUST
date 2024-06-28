def find_first_occurence(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return  -1
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
print(find_first_occurence(arr, target))

print("Binary search is essentially, it takes data and makes a tree. ")
print("mid is the mid point it divides the search")
print("if the target is met it will print the target")
print("if the target is in the right half it will search right which is addition")
print("if the target is left it will subtract")
# Binary search is an algorithm used to efficiently find a target value in a sorted array.
# - It begins by examining the middle element of the array (midpoint).
# - If the middle element matches the target, the search is successful and may print or return the target.
# - If the target is greater than the middle element, the search continues in the right half of the array.
# - If the target is less than the middle element, the search continues in the left half of the array.
