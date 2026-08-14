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
    

    
    x_train,x_test,y_train, y_test= train_test_split(x,y,test_size=0.5,random_state=42)

    model = DecisionTreeClassifier(max_depth=1, random_state=42)
    model= model.fit(x_train,y_train)   
    # Testing accuracy model 1
    test_pred1 = model.predict(x_test)
    testing_accuracy_model= accuracy_score(y_test, test_pred1) * 100

    new_student = pd.DataFrame({
        "StudyHours": [6],
        "Attendance": [85],
        "PreviousScore": [66],
        "AssignmentsCompleted": [1],
        "SleepHours": [7]
    })

    prediction = model.predict(new_student)

    print("New Student Prediction:", prediction[0])

    if prediction[0] == 1:
        print("Student is predicted to PASS")
    else:
        print("Student is predicted to FAIL")
 
   
if __name__ =="__main__":
    main()