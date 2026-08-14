from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot  as  plt

def main():
    # print("hello python")
    datapath= "student_performance_ml.csv"
    df= pd.read_csv(datapath)
    
    # x- independent variable - Features
    # y- dependent variable - Labels

    feature_cols=["StudyHours",
              "Attendance",
              "PreviousScore",
              "AssignmentsCompleted",
              "SleepHours"
              ]

    x = df[feature_cols]
    y = df["FinalResult"]

    print("X shape", x.shape)
    print("y shape", y.shape)
    
    model = DecisionTreeClassifier()
    
    x_train,x_test,y_train, y_test= train_test_split(x,y,test_size=0.5,random_state=42)

    model= model.fit(x_train,y_train)   

    # Training accuracy
    train_pred = model.predict(x_train)
    training_accuracy = accuracy_score(y_train, train_pred) * 100

    # Testing accuracy
    test_pred = model.predict(x_test)
    testing_accuracy = accuracy_score(y_test, test_pred) * 100

    print("Training Accuracy:", training_accuracy, "%")
    print("Testing Accuracy:", testing_accuracy, "%")


    
if __name__ =="__main__":
    main()