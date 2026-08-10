import pandas as pd

border= "-"*30
########################
# step 1 load the dataset
########################
print(border)
print("step 1 load the student dataset")
print(border)

datapath ="student_performance_ml.csv"

df = pd.read_csv(datapath)

print("dataset loaded successfully: ")

print("initial 5 entries from dataset are : ")

print(df.head())

print("last 5 entries from dataset are : ")

print(df.tail())


print(f"total no of rows : {df.shape[0]} and total no of columns : {df.shape[1]}")

# list column names
print("column names :", list(df.columns))
# data types of each column
print("data types of each column :" )    
print(df.dtypes)







