import pandas as pd
import os
def screenclear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

data = {
    'Name': ['John', 'Jessica', 'Micheal', 'Chu', 'Greg'],
    'Age':  [30, 90, 10, 24, 41],
    'State': ['Florida', 'Rhode Island', 'New Mexico', 'California', 'New York']
}
df = pd.DataFrame(data=data)

old: pd.DataFrame = df[df['Age'] > 40]
young: pd.DataFrame = df[df['Age'] < 40]
screenclear()
sort: str = input("How do you want sorted: ")
if sort == 'old':
    print(old)
elif sort == 'young':
    print(young)
else:
    print(df)