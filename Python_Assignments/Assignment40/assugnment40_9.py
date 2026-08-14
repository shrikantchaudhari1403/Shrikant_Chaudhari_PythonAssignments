from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt


def main():

    # ==========================================
    # 1. Load Dataset
    # ==========================================

    df = pd.read_csv("student_performance_ml.csv")


    # ==========================================
    # 2. Create New Feature
    # ==========================================

    df["PerformanceIndex"] = (
        (df["StudyHours"] * 2) + df["Attendance"]
    )


    # Display the new column
    print("\n===== Dataset with PerformanceIndex =====")
    print(df)


    # ==========================================
    # 3. Features WITHOUT PerformanceIndex
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
    # 4. Train/Test Split
    # ==========================================

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.5,
        random_state=42
    )


    # ==========================================
    # 5. Model WITHOUT PerformanceIndex
    # ==========================================

    model1 = DecisionTreeClassifier(random_state=42)

    model1.fit(x_train, y_train)

    y_pred1 = model1.predict(x_test)

    accuracy1 = accuracy_score(y_test, y_pred1)


    print("\n===== Accuracy WITHOUT PerformanceIndex =====")

    print(f"Accuracy: {accuracy1 * 100:.2f}%")


    # ==========================================
    # 6. Features WITH PerformanceIndex
    # ==========================================

    feature_col_new = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours",
        "PerformanceIndex"
    ]

    x_new = df[feature_col_new]

    y_new = df["FinalResult"]


    # ==========================================
    # 7. Train/Test Split
    # ==========================================

    x_train_new, x_test_new, y_train_new, y_test_new = train_test_split(
        x_new,
        y_new,
        test_size=0.5,
        random_state=42
    )


    # ==========================================
    # 8. Model WITH PerformanceIndex
    # ==========================================

    model2 = DecisionTreeClassifier(random_state=42)

    model2.fit(x_train_new, y_train_new)

    y_pred2 = model2.predict(x_test_new)

    accuracy2 = accuracy_score(y_test_new, y_pred2)


    print("\n===== Accuracy WITH PerformanceIndex =====")

    print(f"Accuracy: {accuracy2 * 100:.2f}%")


    # ==========================================
    # 9. Compare Accuracy
    # ==========================================

    print("\n===== Accuracy Comparison =====")

    print(f"Without PerformanceIndex: {accuracy1 * 100:.2f}%")

    print(f"With PerformanceIndex:    {accuracy2 * 100:.2f}%")


    if accuracy2 > accuracy1:

        print("\nAccuracy INCREASED.")

    elif accuracy2 < accuracy1:

        print("\nAccuracy DECREASED.")

    else:

        print("\nAccuracy DID NOT CHANGE.")


    # ==========================================
    # 10. Display Improvement
    # ==========================================

    improvement = (accuracy2 - accuracy1) * 100

    print(f"Accuracy change: {improvement:.2f} percentage points")


    # ==========================================
    # 11. Plot New Decision Tree
    # ==========================================

    plt.figure(figsize=(16, 10))

    plot_tree(
        model2,
        filled=True,
        feature_names=feature_col_new,
        class_names=[str(x) for x in model2.classes_]
    )

    plt.title("Decision Tree with PerformanceIndex")

    plt.show()


if __name__ == "__main__":
    main()