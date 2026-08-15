import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)

import matplotlib.pyplot as plt


def main():

    # --------------------------------------------------
    # 1. Load dataset
    # --------------------------------------------------
    path = "WinePredictor.csv"

    df = pd.read_csv(path)

    print("First 5 records:")
    print(df.head())

    print("\nDataset shape:")
    print(df.shape)

    print("\nColumn names:")
    print(df.columns)

    # --------------------------------------------------
    # 2. Check missing values
    # --------------------------------------------------
    print("\nMissing values:")
    print(df.isnull().sum())

    # Remove duplicate records if any
    df = df.drop_duplicates()

    print("\nShape after removing duplicates:")
    print(df.shape)

    # --------------------------------------------------
    # 3. Separate Features and Target
    # --------------------------------------------------

    # X = independent variables / features
    feature_columns = [
        "Alcohol",
        "Malic acid",
        "Ash",
        "Alcalinity of ash",
        "Magnesium",
        "Total phenols",
        "Flavanoids",
        "Nonflavanoid phenols",
        "Proanthocyanins",
        "Color intensity",
        "Hue",
        "OD280/OD315 of diluted wines",
        "Proline"
    ]

    X = df[feature_columns]

    # y = dependent variable / target
    y = df["Class"]

    print("\nFeatures:")
    print(X.head())

    print("\nTarget:")
    print(y.head())

    # --------------------------------------------------
    # 4. Train-Test Split
    # --------------------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("\nTraining data:", X_train.shape)
    print("Testing data:", X_test.shape)

    # --------------------------------------------------
    # 5. Feature Scaling
    # --------------------------------------------------

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # --------------------------------------------------
    # 6. Create Machine Learning Model
    # --------------------------------------------------

    model = DecisionTreeClassifier(random_state=42)

    # --------------------------------------------------
    # 7. Train Model
    # --------------------------------------------------

    model.fit(X_train, y_train)

    # --------------------------------------------------
    # 8. Make Predictions
    # --------------------------------------------------

    y_pred = model.predict(X_test)

    print("\nActual values:")
    print(y_test.values)

    print("\nPredicted values:")
    print(y_pred)

    # --------------------------------------------------
    # 9. Calculate Accuracy
    # --------------------------------------------------

    accuracy = accuracy_score(y_test, y_pred)

    print("\nAccuracy:")
    print(accuracy)

    print("\nAccuracy Percentage:")
    print(accuracy * 100, "%")

    # --------------------------------------------------
    # 10. Confusion Matrix
    # --------------------------------------------------

    cm = confusion_matrix(y_test, y_pred)

    print("\nConfusion Matrix:")
    print(cm)

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=[1, 2, 3]
    )

    disp.plot()

    plt.title("Wine Classification - Confusion Matrix")
    plt.show()

    # --------------------------------------------------
    # 11. Classification Report
    # --------------------------------------------------

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    main()