from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as ply
import pandas as pd




def main():
    path= "student_performance_ml.csv"
    df= pd.read_csv(path)
    #print(dataset)
    
    feature_col= ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]
    
    x=df[feature_col]
    y=df["FinalResult"]

    ply.figure(figsize=(8,5))
    ply.scatter(df["StudyHours"],df["PreviousScore"]) 
     
    ply.xlabel("Study Hours")
    ply.ylabel("Previous Score")
    ply.title("Study Hours vs Previous Score")

    ply.grid()
    ply.show()

    X_train, X_test, Y_train, Y_test=train_test_split(x,y,test_size=0.5,random_state=42)

    model= DecisionTreeClassifier()

    model= model.fit(X_train,Y_train)

    y_pred= model.predict(X_test)

    result= accuracy_score(Y_test,y_pred)

    print("accuracy Score :", result)

    feture_Importance= model.feature_importances_

    for feature,score in zip(feature_col,feture_Importance):

        print(
            feature,
            ":",
            round(score, 4)
        )

     
  
if __name__=="__main__":
    main()