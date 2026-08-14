from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

import pandas as pd

def main():
    path="student_performance_ml.csv"
    df= pd.read_csv(path)
    feature_col=["StudyHours","Attendance"]

    x= df[feature_col] 
    y= df["FinalResult"]

    x_train, x_test, y_train, y_test= train_test_split(x,y,test_size=0.5, random_state=42)

    model= DecisionTreeClassifier(random_state=42)

    model.fit(x_train,y_train)

    y_pred= model.predict(x_test)

    result= accuracy_score(y_test,y_pred)

    print(f"model Accurancy : {round(result * 100,2)}")


if __name__ =="__main__":
    main()
