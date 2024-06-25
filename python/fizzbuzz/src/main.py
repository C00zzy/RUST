import os 
os.system('clear')

num = 0
while (num <= 100): # This is a comment
    if (num % 3 == 0) and (num % 5 == 0):
        print (str(num) + ": fizzbuzz!")
    
    elif (num % 3 == 0):
        print(str(num) + ": Fizz!")
    elif (num % 5 == 0):
        print(str(num) + ": Fizz!")
    else:
        print(str(num) + '.')
    
    print(num)
    num +=1
    
    