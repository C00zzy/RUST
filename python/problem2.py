import pandas as pd

data = {
    'Name': ['John', 'Jessica', 'Micheal', 'Chu', 'Greg'],
    'Age':  [30, 90, 10, 24, 41],
    'State': ['Florida', 'Rhode Island', 'New Mexico', 'California', 'New York']
}
# Sort the data
def sortthedata(data) -> None:
    df = pd.DataFrame(data=data)
    print(df)
sortthedata(data=data)