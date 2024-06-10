import os
import random

# text editor
def textedit():
    print("Text editor")
    lines = [] 
    while True:
        line = input(">")
        
        if line.lower() == 'exit':
            break
        else:
            lines.append(line)
        with open("test.txt", "w") as file:
            file.write("\n".join(lines))
        print("saved")
        
textedit()
    
    