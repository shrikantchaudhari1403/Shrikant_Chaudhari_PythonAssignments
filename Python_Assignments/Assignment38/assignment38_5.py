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

# Average study hours by final result
study_hours = df.groupby("FinalResult")["StudyHours"].mean()

# Average attendance by final result
attendance = df.groupby("FinalResult")["Attendance"].mean()

print("Average Study Hours:")
print(study_hours)

print("\nAverage Attendance:")
print(attendance)