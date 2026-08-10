import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_performance_ml.csv")

# Separate pass and fail students
passed = df[df["FinalResult"] == 1]
failed = df[df["FinalResult"] == 0]

# Scatter plot for failed students
plt.scatter(
    failed["StudyHours"],
    failed["PreviousScore"],
    label="Fail"
)

# Scatter plot for passed students
plt.scatter(
    passed["StudyHours"],
    passed["PreviousScore"],
    label="Pass"
)

# Labels and title
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Study Hours vs Previous Score - Pass vs Fail")

# Legend and grid
plt.legend()
plt.grid(True)

# Display plot
plt.show()