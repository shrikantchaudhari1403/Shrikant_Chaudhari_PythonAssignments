from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd


def main():

    # ==========================================
    # 1. Load Dataset
    # ==========================================

    datapath = "student_performance_ml.csv"

    df = pd.read_csv(datapath)

    print("===== Original Dataset =====")
    print(df)


    # ==========================================
    # 2. Select Features and Target
    # ==========================================

    feature_col = ["StudyHours", "Attendance"]

    x = df[feature_col]

    y = df["FinalResult"]


    # ==========================================
    # 3. Split Dataset
    # ==========================================

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42
    )


    print("\n===== Training Data =====")
    print(x_train)

    print("\n===== Testing Data =====")
    print(x_test)


    # ==========================================
    # 4. Create Decision Tree Model
    # ==========================================

    model = DecisionTreeClassifier(random_state=42)


    # ==========================================
    # 5. Train Model
    # ==========================================

    model.fit(x_train, y_train)


    # ==========================================
    # 6. Predict Test Data
    # ==========================================

    y_pred = model.predict(x_test)


    print("\n===== Actual vs Predicted =====")

    for i in range(len(y_test)):

        print(
            "Actual:",
            y_test.iloc[i],
            "| Predicted:",
            y_pred[i]
        )


    # ==========================================
    # 7. Manual Accuracy Calculation
    # ==========================================

    correct = 0

    for i in range(len(y_test)):

        if y_test.iloc[i] == y_pred[i]:
            correct += 1

    total = len(y_test)

    manual_accuracy = (correct / total) * 100


    print("\n===== Manual Accuracy =====")

    print("Correct Predictions:", correct)

    print("Total Predictions:", total)

    print("Manual Accuracy:", manual_accuracy, "%")


    # ==========================================
    # 8. Sklearn Accuracy
    # ==========================================

    sklearn_accuracy = accuracy_score(
        y_test,
        y_pred
    ) * 100


    print("\n===== Sklearn Accuracy =====")

    print("Sklearn Accuracy:", sklearn_accuracy, "%")


    # ==========================================
    # 9. Verify Accuracy
    # ==========================================

    print("\n===== Accuracy Verification =====")

    if manual_accuracy == sklearn_accuracy:

        print("Both accuracies MATCH")

    else:

        print("Both accuracies DO NOT MATCH")


    # ==========================================
    # 10. Identify Incorrect Predictions
    # ==========================================

    result_df = x_test.copy()

    result_df["ActualResult"] = y_test

    result_df["PredictedResult"] = y_pred


    incorrect_students = result_df[
        result_df["ActualResult"] != result_df["PredictedResult"]
    ]


    print("\n===== Incorrect Predictions =====")

    if len(incorrect_students) > 0:

        print(incorrect_students)

    else:

        print("No incorrect predictions")


    # ==========================================
    # 11. Create 5 New Students
    # ==========================================

    new_students = pd.DataFrame({

        "StudyHours": [2, 5, 7, 3, 9],

        "Attendance": [60, 75, 90, 65, 95]

    })


    print("\n===== New Students =====")

    print(new_students)


    # ==========================================
    # 12. Predict New Students
    # ==========================================

    new_predictions = model.predict(new_students)


    # ==========================================
    # 13. Add Predictions to DataFrame
    # ==========================================

    new_students["PredictedResult"] = new_predictions


    # ==========================================
    # 14. Display New Student Predictions
    # ==========================================

    print("\n===== New Student Predictions =====")

    print(new_students)


# ==========================================
# Run Program
# ==========================================

if __name__ == "__main__":
    main()