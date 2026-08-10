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

# Distribution of FinalResult
result_counts = df['FinalResult'].value_counts()

print("\nFinal Result Distribution:")
print(result_counts)


# Percentage distribution
result_percentage = df['FinalResult'].value_counts(normalize=True) * 100

print("\nFinal Result Percentage:")
print(result_percentage)

print(f"\nPass percentage: {result_percentage[1]:.2f}%")
print(f"Fail percentage: {result_percentage[0]:.2f}%")