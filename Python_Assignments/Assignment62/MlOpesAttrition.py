import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

import matplotlib.pyplot as plt


# ============================================================
# STEP 1: LOAD DATASET
# ============================================================

data = pd.read_csv("Employee_Attrition.csv")


# ============================================================
# STEP 2: UNDERSTAND THE DATA
# ============================================================

print("Shape:")
print(data.shape)

print("\nColumns:")
print(data.columns)

print("\nFirst 5 rows:")
print(data.head())

print("\nStatistical Summary:")
print(data.describe())


# ============================================================
# STEP 3: CHECK FOR MISSING VALUES
# ============================================================

print("\nMissing Value Count:")
print(data.isna().sum())


# ============================================================
# STEP 4: ENCODE CATEGORICAL FEATURES
# ============================================================

# One-hot encoding for OverTime
data = pd.get_dummies(
    data,
    columns=["OverTime"],
    dtype=int
)

# Binary encoding for target variable
data["Attrition"] = data["Attrition"].map({
    "Yes": 1,
    "No": 0
})


# ============================================================
# STEP 5: CHECK FINAL DATASET
# ============================================================

print("\nFinal Dataset:")
print(data.head())

print("\nFinal Columns:")
print(data.columns)


# ============================================================
# STEP 6: SEPARATE FEATURES AND LABEL
# ============================================================

X = data.drop(columns=["Attrition"])
Y = data["Attrition"]

print("\nFeatures:")
print(X)

print("\nLabel:")
print(Y)

print("\nFeature Columns:")
print(X.columns.tolist())


# ============================================================
# STEP 7: DIVIDE DATASET INTO TRAINING AND TESTING
# ============================================================

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.3,
    random_state=42
)


# ============================================================
# STEP 8: FEATURE SCALING
# ============================================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)


# ============================================================
# STEP 9: CREATE MLP NEURAL NETWORK
# ============================================================

model = MLPClassifier(
    hidden_layer_sizes=(4, 3),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)


# ============================================================
# STEP 10: TRAIN THE MODEL
# ============================================================

model.fit(X_train_scaled, Y_train)


# ============================================================
# STEP 11: DISPLAY TRAINING INFORMATION
# ============================================================

print("\nNumber of iterations used for training:")
print(model.n_iter_)


# ============================================================
# STEP 12: TESTING ACCURACY
# ============================================================

Y_test_pred = model.predict(X_test_scaled)

testing_accuracy = accuracy_score(
    Y_test,
    Y_test_pred
)

print("\nTesting Accuracy:")
print(testing_accuracy * 100, "%")


# ============================================================
# STEP 13: TRAINING ACCURACY
# ============================================================

Y_train_pred = model.predict(X_train_scaled)

training_accuracy = accuracy_score(
    Y_train,
    Y_train_pred
)

print("\nTraining Accuracy:")
print(training_accuracy * 100, "%")


# ============================================================
# STEP 14: CONFUSION MATRIX
# ============================================================

print("\nConfusion Matrix:")

print(confusion_matrix(
    Y_test,
    Y_test_pred
))


# ============================================================
# STEP 15: PREDICTION FUNCTION
# ============================================================

def predictAttrition(employeeData):

    # Convert employee data into DataFrame
    employee_df = pd.DataFrame([employeeData])

    # One-hot encode OverTime
    employee_df = pd.get_dummies(
        employee_df,
        columns=["OverTime"],
        dtype=int
    )

    # Make sure employee has exactly
    # the same columns as training data
    employee_df = employee_df.reindex(
        columns=X.columns,
        fill_value=0
    )

    # Apply the same scaler used during training
    employee_scaled = scaler.transform(employee_df)

    # Make prediction
    prediction = model.predict(employee_scaled)[0]

    # Get probability of Attrition = Yes
    probability = model.predict_proba(
        employee_scaled
    )[0][1]

    # Convert prediction into readable result
    if prediction == 1:

        result = "Yes - Employee may leave the company"

    else:

        result = "No - Employee may stay in the company"

    return result, probability * 100


# ============================================================
# STEP 16: TEST WITH 5 NEW EMPLOYEES
# ============================================================

employees = [

    {
        "Age": 25,
        "DailyRate": 800,
        "DistanceFromHome": 5,
        "HourlyRate": 80,
        "JobLevel": 1,
        "MonthlyIncome": 3000,
        "MonthlyRate": 12000,
        "NumCompaniesWorked": 1,
        "PercentSalaryHike": 12,
        "PerformanceRating": 3,
        "TotalWorkingYears": 2,
        "YearsAtCompany": 1,
        "YearsInCurrentRole": 0,
        "YearsSinceLastPromotion": 0,
        "YearsWithCurrManager": 0,
        "OverTime": "Yes"
    },

    {
        "Age": 40,
        "DailyRate": 1200,
        "DistanceFromHome": 15,
        "HourlyRate": 60,
        "JobLevel": 3,
        "MonthlyIncome": 8000,
        "MonthlyRate": 20000,
        "NumCompaniesWorked": 4,
        "PercentSalaryHike": 18,
        "PerformanceRating": 4,
        "TotalWorkingYears": 15,
        "YearsAtCompany": 10,
        "YearsInCurrentRole": 5,
        "YearsSinceLastPromotion": 2,
        "YearsWithCurrManager": 5,
        "OverTime": "No"
    },

    {
        "Age": 30,
        "DailyRate": 500,
        "DistanceFromHome": 25,
        "HourlyRate": 50,
        "JobLevel": 1,
        "MonthlyIncome": 3500,
        "MonthlyRate": 10000,
        "NumCompaniesWorked": 3,
        "PercentSalaryHike": 11,
        "PerformanceRating": 3,
        "TotalWorkingYears": 5,
        "YearsAtCompany": 2,
        "YearsInCurrentRole": 1,
        "YearsSinceLastPromotion": 0,
        "YearsWithCurrManager": 1,
        "OverTime": "Yes"
    },

    {
        "Age": 50,
        "DailyRate": 1000,
        "DistanceFromHome": 3,
        "HourlyRate": 70,
        "JobLevel": 4,
        "MonthlyIncome": 10000,
        "MonthlyRate": 25000,
        "NumCompaniesWorked": 2,
        "PercentSalaryHike": 20,
        "PerformanceRating": 4,
        "TotalWorkingYears": 25,
        "YearsAtCompany": 15,
        "YearsInCurrentRole": 8,
        "YearsSinceLastPromotion": 3,
        "YearsWithCurrManager": 7,
        "OverTime": "No"
    },

    {
        "Age": 28,
        "DailyRate": 600,
        "DistanceFromHome": 20,
        "HourlyRate": 90,
        "JobLevel": 2,
        "MonthlyIncome": 4500,
        "MonthlyRate": 14000,
        "NumCompaniesWorked": 2,
        "PercentSalaryHike": 13,
        "PerformanceRating": 3,
        "TotalWorkingYears": 6,
        "YearsAtCompany": 3,
        "YearsInCurrentRole": 1,
        "YearsSinceLastPromotion": 1,
        "YearsWithCurrManager": 1,
        "OverTime": "Yes"
    }
]


# ============================================================
# STEP 17: PREDICT ALL 5 EMPLOYEES
# ============================================================

print("\n")
print("=" * 60)
print("ATTRITION PREDICTION FOR NEW EMPLOYEES")
print("=" * 60)


for i, employee in enumerate(employees, start=1):

    result, probability = predictAttrition(employee)

    print("\nEmployee", i)
    print("-" * 40)

    print("Age:", employee["Age"])

    print("OverTime:", employee["OverTime"])

    print("Attrition:", result)

    print(
        "Attrition Probability:",
        round(probability, 2),
        "%"
    )


# ============================================================
# STEP 18: PLOT LOSS CURVE
# ============================================================

plt.plot(model.loss_curve_)

plt.xlabel("Iterations")
plt.ylabel("Loss")

plt.title("MLP Training Loss Curve")

plt.show()