import queue

def process():
    q = queue.Queue()

    while True:
        usr_input = input("Enter value or exit to exit")
        if usr_input.lower() == 'exit':
            break
        q.put(usr_input)
        
        print("Processing the input:")
        while not q.empty():
            value = q.get()
            print("processing:", value)
process()