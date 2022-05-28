import pandas as pd

data = pd.read_excel('Data\EU COUNTRIES_rail passengers_quarterly data since 2019-Q4.xlsx')
df = pd.DataFrame(data, index=[2], columns=['Country','2021-Q4'])
print("Here are the Values for: ")
print(df)