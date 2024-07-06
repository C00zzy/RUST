import pandas as pd # type: ignore
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

old: pd.DataFrame = df[df['Age'] > 40] # type: ignore
young: pd.DataFrame = df[df['Age'] < 40] # type: ignore
screenclear()
sort: str = input("How do you want sorted: ")
if sort == 'old' and sort == 'age':
    print(old)
elif sort == 'young':
    print(young)
else:
    print(df)