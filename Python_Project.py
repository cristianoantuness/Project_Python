import pandas as pd

data = pd.read_excel(r'C:\Users\Crist\OneDrive - Hochschule Luzern\International Business Administration IBA\Semester 06\Programming with Phyton\Project_Python\Data\EU COUNTRIES_rail passengers_quarterly data since 2019-Q4.xlsx')
df = pd.DataFrame(data, index=[2], columns=['Country','2021-Q4'])
print("Here are the Values for: ")
print(df)