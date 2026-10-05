import pandas as pd 

# 2.1
# print("Hello World")

# 2.2
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame)

# 03

# 04
# ages = pd.Series([23,45,7,34,6,63,36,78,54,34])
# print(ages)

# 04.1
# date_series = pd.date_range(start = '2021-05-01', end = '2021-05-12')
# print(date_series)

# 4.2
# my_series = pd.Series([2, 4, 6, 8, 10])
# modified_series = my_series.apply(lambda x:x/2)
# print(modified_series)

# 05
# data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
# df = pd.DataFrame(data, columns=['Brand', 'Model', 'Color'])
# print(df)

# 5.1
# data = [
#     { 
#         "brand": "Toyota", 
#         "model": "Corolla",
#         "color": "Blue"
#     },
#     {
#         "brand": "Ford", 
#         "model": "K",
#         "color": "Yellow"
#     },
#     {
#         "brand": "Porsche", 
#         "model": "Cayenne",
#         "color": "White"
#     },
#     {
#         "brand": "Tesla", 
#         "model": "Model S",
#         "color": "Red"
#     }

# df = pd.DataFrame(data)
# print(df)

# 5.2
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame.iloc[133,6])

# 5.3
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# We can read only the first 3 rows
# print(data_frame.head(3))

# 5.4
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# We can read only the last 3 rows
# print(data_frame.tail(3))

# 5.5
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame[['Name', 'Type 1']][0:10])

# 5.6
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame.loc[data_frame['Attack'] > 80])

# 5.7
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(len(data_frame.loc[data_frame['Legendary'] == True]))

# 06
# data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
# print(data_frame.head(5))

# 6.1
# data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
# del data_frame[data_frame.columns[0]]
# print(data_frame.head(5))

# 6.2
# data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
# count = data_frame['Gender'].value_counts()
# print(count)

# 6.3
data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
names = data_frame.groupby("Name").sum()
print(len(names))