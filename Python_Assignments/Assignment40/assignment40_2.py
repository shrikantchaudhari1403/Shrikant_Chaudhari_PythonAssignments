from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as ply
import pandas as pd


def main():
    # ==========================================
    # 1. Load Dataset
    # ==========================================
    path = "student_performance_ml.csv"
    df = pd.read_csv(path)
    # ==========================================
    # 2. Features - Original Model
    # ==========================================
    feature_col = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]
    x = df[feature_col]
    y = df["FinalResult"]
    # ==========================================
    # 3. Train Test Split
    # ==========================================
    X_train, X_test, Y_train, Y_test = train_test_split(
        x,
        y,
        test_size=0.5,
        random_state=42
    )
    # ==========================================
    # 4. Original Model
    # ==========================================
    model1 = DecisionTreeClassifier(
        random_state=42
    )
    model1.fit(X_train, Y_train)
    y_pred1 = model1.predict(X_test)
    accuracy1 = accuracy_score(
        Y_test,
        y_pred1
    )

    print("\n========== ORIGINAL MODEL ==========")
    print("Features used:")
    print(feature_col)
    print("Accuracy:", accuracy1)
    print("Accuracy %:", round(accuracy1 * 100, 2))
    # ==========================================
    # 5. Remove SleepHours
    # ==========================================
    feature_col_without_sleep = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted"
    ]

    x_without_sleep = df[feature_col_without_sleep]
    # Use the SAME train/test split
    X_train2, X_test2, Y_train2, Y_test2 = train_test_split(
        x_without_sleep,
        y,
        test_size=0.5,
        random_state=42
    )
    # ==========================================
    # 6. Train New Model
    # ==========================================
    model2 = DecisionTreeClassifier(
        random_state=42
    )
    model2.fit(X_train2, Y_train2)
    y_pred2 = model2.predict(X_test2)

    accuracy2 = accuracy_score(
        Y_test2,
        y_pred2
    )

    print("\n========== MODEL WITHOUT SLEEPHOURS ==========")
    print("Features used:")
    print(feature_col_without_sleep)
    print("Accuracy:", accuracy2)
    print("Accuracy %:", round(accuracy2 * 100, 2))

    # ==========================================
    # 7. Compare Accuracies
    # ==========================================

    print("\n========== ACCURACY COMPARISON ==========")
    print(
        "Original Accuracy:",
        round(accuracy1 * 100, 2),
        "%"
    )

    print(
        "New Accuracy:",
        round(accuracy2 * 100, 2),
        "%"
    )

    # ==========================================
    # 8. Calculate Difference
    # ==========================================

    difference = accuracy2 - accuracy1

    print(
        "Accuracy Difference:",
        round(difference * 100, 2),
        "percentage points"
    )

    # ==========================================
    # 9. Final Conclusion
    # ==========================================

    print("\n========== FINAL CONCLUSION ==========")

    if accuracy2 > accuracy1:
        print(
            "Removing SleepHours IMPROVED the model performance."
        )

    elif accuracy2 < accuracy1:
        print(
            "Removing SleepHours REDUCED the model performance."
        )
    else:

        print(
            "Removing SleepHours had NO EFFECT on the model accuracy."
        )

if __name__ == "__main__":
    main()