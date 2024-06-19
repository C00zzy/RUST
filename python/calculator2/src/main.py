#### PUSEDO CODE ####
#  inputforcal func:
#       input("Enter two number):
#       Then store both as variable
#       after return to outside of func
#       exit
#
#   addition func:
#       sum = number 1 + number 2
#       exit
##   multiply func:
 #      sum = number 1 * number 2
 #      exit
#
#
#   logicforcal func:
#       (inputforcal)
#           input("What operator:   )
#           then
#### PUSEDO CODE ####

def inputforcal():
    while True:
        try:
            num1, num2, = input("Enter two number seperated by a comma:  ").split(',')
            
            num1 = float(num1.strip())
            num2 = float(num2.strip()) 
            
            print("Numbers Selected and converted to floating! Numbers:  ",num1 ,num2)
            return num1, num2
        except ValueError:
            print("Invalid")


def funcforcal(num1, num2):
    sum = num1 + num2

# TODO Add funcutions for addition, subtraction, divison