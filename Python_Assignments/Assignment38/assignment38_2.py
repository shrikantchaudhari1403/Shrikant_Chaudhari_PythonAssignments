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

print(f"total no of students : {df.shape[0]}")

print(f"total pass students count : {df[df['FinalResult'] == 1].shape[0]}")

print(f"total fail students count : {df[df['FinalResult'] == 0].shape[0]}")