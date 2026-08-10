import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset
datapath = "student_performance_ml.csv"

df = pd.read_csv(datapath)

print("Dataset loaded successfully")
print(f"Total students: {df.shape[0]}")

# Step 2: Plot histogram of StudyHours
plt.hist(df["StudyHours"], bins=8, edgecolor="black")

# Step 3: Add labels and title
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.title("Distribution of Study Hours")

# Step 4: Display histogram
plt.show()