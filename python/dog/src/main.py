def dogyears():
    while True:
        try:
            num1 = int(input("What is your age:  "))
            result = num1 * 7
            print(result)
            break
        except KeyboardInterrupt:
            print("Exiting")
            break
dogyears()