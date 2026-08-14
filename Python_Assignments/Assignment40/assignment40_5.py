from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd


def main():

    # ---------------------------------------
    # 1. Load dataset
    # ---------------------------------------

    datapath = "student_performance_ml.csv"

    df = pd.read_csv(datapath)

    print("Original Dataset:")
    print(df)


    # ---------------------------------------
    # 2. Select Features and Target
    # ---------------------------------------

    feature_col = ["StudyHours", "Attendance"]

    x = df[feature_col]
    y = df["FinalResult"]


    # ---------------------------------------
    # 3. Split data into training and testing
    # ---------------------------------------

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42
    )


    # ---------------------------------------
    # 4. Create Decision Tree model
    # ---------------------------------------

    model = DecisionTreeClassifier(random_state=42)


    # ---------------------------------------
    # 5. Train the model
    # ---------------------------------------

    model.fit(x_train, y_train)


    # ---------------------------------------
    # 6. Predict test data
    # ---------------------------------------

    y_pred = model.predict(x_test)

    print("\nActual Results:")
    print(y_test.values)

    print("\nPredicted Results:")
    print(y_pred)


    # ---------------------------------------
    # 7. Calculate Accuracy Manually
    # ---------------------------------------

    correct = 0

    for i in range(len(y_test)):

        if y_test.iloc[i] == y_pred[i]:
            correct += 1

    total = len(y_test)

    manual_accuracy = (correct / total) * 100


    print("\n----- Manual Accuracy -----")
    print("Correct Predictions:", correct)
    print("Total Predictions:", total)
    print("Manual Accuracy:", manual_accuracy, "%")


    # ---------------------------------------
    # 8. Calculate Accuracy using sklearn
    # ---------------------------------------

    sklearn_accuracy = accuracy_score(y_test, y_pred) * 100

    print("\n----- Sklearn Accuracy -----")
    print("Sklearn Accuracy:", sklearn_accuracy, "%")


    # ---------------------------------------
    # 9. Verify both accuracies
    # ---------------------------------------

    print("\n----- Accuracy Verification -----")

    if manual_accuracy == sklearn_accuracy:
        print("Both accuracies MATCH")
    else:
        print("Both accuracies DO NOT MATCH")


    # ---------------------------------------
    # 10. Create 5 New Students
    # ---------------------------------------

    new_students = pd.DataFrame({

        "StudyHours": [2, 5, 7, 3, 9],

        "Attendance": [60, 75, 90, 65, 95]

    })


    print("\n----- New Students -----")

    print(new_students)


    # ---------------------------------------
    # 11. Predict New Students
    # ---------------------------------------

    new_predictions = model.predict(new_students)


    # ---------------------------------------
    # 12. Add predictions to DataFrame
    # ---------------------------------------

    new_students["PredictedResult"] = new_predictions


    # ---------------------------------------
    # 13. Display final predictions
    # ---------------------------------------

    print("\n----- New Students Predictions -----")

    print(new_students)


# ---------------------------------------
# Run program
# ---------------------------------------

if __name__ == "__main__":
    main()