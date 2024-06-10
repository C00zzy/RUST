import os 
os.system('clear')

num = 0
while (num <= 100):
    if (num % 3 == 0) and (num % 5 == 0):
        print (str(num) + ": fizzbuzz!")
    
    elif (num % 3 == 0):
        print(str(num) + ": Fizz!")
    
    print(num)
    num +=1
    
    