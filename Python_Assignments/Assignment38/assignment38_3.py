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

print(f"Average study hours of students : {df['StudyHours'].mean()}")

print(f"Average attendance of students : {df['Attendance'].mean()}")

print(f"maximum privious year marks of students : {df['PreviousScore'].max()}")

print(f"minimum sleep hours of students : {df['SleepHours'].min()}")