books = [
     "A Tale of Two Cities", "Brave New World", "Catch-22", "Don Quixote",
    "Great Expectations", "Moby Dick", "Pride and Prejudice",
    "The Catcher in the Rye", "The Great Gatsby", "To Kill a Mockingbird"
]

def bookfinder(books, target):
    low, high = 0, len(books) - 1
    target = target.lower()

    while low <= high:
        mid = (low + high) // 2
        mid_book = books[mid].lower()
        if mid_book == target:
            return mid
        elif mid_book < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
    