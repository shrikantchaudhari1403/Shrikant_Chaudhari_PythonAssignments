from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

import pandas as pd
import matplotlib.pyplot as plt


def main():

    # ==========================================================
    # 1. DATA LOAD
    # ==========================================================
    print("\n========== DATA LOAD ==========")

    datapath = "student_performance_ml.csv"

    df = pd.read_csv(datapath)

    print("Dataset loaded successfully!")
    print("Number of rows:", df.shape[0])
    print("Number of columns:", df.shape[1])


    # ==========================================================
    # 2. DATA ANALYSIS
    # ==========================================================
    print("\n========== DATA ANALYSIS ==========")

    # Display first 5 rows
    print("\nFirst 5 rows:")
    print(df.head())

    # Display column names
    print("\nColumn names:")
    print(df.columns)

    # Display data types
    print("\nData types:")
    print(df.dtypes)

    # Check missing values
    print("\nMissing values:")
    print(df.isnull().sum())

    # Statistical analysis
    print("\nStatistical summary:")
    print(df.describe())

    # Final result distribution
    print("\nFinal Result count:")
    print(df["FinalResult"].value_counts())


    # ==========================================================
    # 3. VISUALIZATION
    # ==========================================================
    print("\n========== VISUALIZATION ==========")
    # ------------------------------
    # Visualization 1
    # Study Hours vs Previous Score
    # ------------------------------
    plt.figure(figsize=(8, 5))

    plt.scatter(
        df["StudyHours"],
        df["PreviousScore"]
    )

    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.title("Study Hours vs Previous Score")

    plt.grid()
    plt.show()


    # ------------------------------
    # Visualization 2
    # Attendance Distribution
    # ------------------------------

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["Attendance"],
        bins=10
    )

    plt.xlabel("Attendance")
    plt.ylabel("Number of Students")
    plt.title("Attendance Distribution")

    plt.grid()
    plt.show()


    # ------------------------------
    # Visualization 3
    # Final Result
    # ------------------------------

    plt.figure(figsize=(6, 4))

    df["FinalResult"].value_counts().plot(
        kind="bar"
    )

    plt.xlabel("Final Result")
    plt.ylabel("Number of Students")
    plt.title("Pass / Fail Distribution")

    plt.show()


    # ==========================================================
    # 4. SELECT FEATURES AND LABEL
    # ==========================================================

    print("\n========== FEATURES AND LABEL ==========")

    feature_cols = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    # Independent variables
    x = df[feature_cols]

    # Dependent variable
    y = df["FinalResult"]

    print("\nFeatures:")
    print(x.head())

    print("\nLabels:")
    print(y.head())

    print("\nX shape:", x.shape)
    print("Y shape:", y.shape)


    # ==========================================================
    # 5. TRAIN / TEST SPLIT
    # ==========================================================

    print("\n========== TRAIN / TEST SPLIT ==========")

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42
    )

    print("Training records:", x_train.shape[0])
    print("Testing records:", x_test.shape[0])


    # ==========================================================
    # 6. MODEL TRAINING
    # ==========================================================

    print("\n========== MODEL TRAINING ==========")

    model = DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    )

    # Train model
    model.fit(x_train, y_train)

    print("Decision Tree model trained successfully!")


    # ==========================================================
    # 7. TEST / PREDICTION
    # ==========================================================

    print("\n========== MODEL TESTING ==========")

    # Predict results for test data
    y_pred = model.predict(x_test)

    print("Actual values:")
    print(y_test.values)

    print("\nPredicted values:")
    print(y_pred)


    # ==========================================================
    # 8. ACCURACY CALCULATION
    # ==========================================================

    print("\n========== ACCURACY ==========")

    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    print("Testing Accuracy:", accuracy)

    print(
        "Testing Accuracy:",
        round(accuracy * 100, 2),
        "%"
    )


    # ==========================================================
    # 9. CONFUSION MATRIX
    # ==========================================================

    print("\n========== CONFUSION MATRIX ==========")

    cm = confusion_matrix(
        y_test,
        y_pred
    )

    print("Confusion Matrix:")
    print(cm)

    # Display confusion matrix
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm
    )

    disp.plot()

    plt.title("Decision Tree - Confusion Matrix")
    plt.show()


    # ==========================================================
    # 10. PREDICT NEW STUDENT
    # ==========================================================

    print("\n========== NEW STUDENT PREDICTION ==========")

    # New student details
    new_student = pd.DataFrame({
        "StudyHours": [6],
        "Attendance": [85],
        "PreviousScore": [66],
        "AssignmentsCompleted": [1],
        "SleepHours": [7]
    })

    print("\nNew Student:")
    print(new_student)

    # Predict
    prediction = model.predict(new_student)

    print("\nPredicted Final Result:", prediction[0])


    # ==========================================================
    # 11. FINAL CONCLUSION
    # ==========================================================

    print("\n========== FINAL CONCLUSION ==========")

    print(
        "The Decision Tree model was successfully trained "
        "using student performance data."
    )

    print(
        "The model was tested using unseen test data."
    )

    print(
        "Testing Accuracy:",
        round(accuracy * 100, 2),
        "%"
    )

    print(
        "The confusion matrix shows the number of "
        "correct and incorrect predictions."
    )

    print(
        "For the new student, the predicted result is:",
        prediction[0]
    )


if __name__ == "__main__":
    main()