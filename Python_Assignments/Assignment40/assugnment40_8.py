from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt


def main():
    df=  pd.read_csv("student_performance_ml.csv") 
    feature_col= ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]
   
    x= df[feature_col]
    y= df["FinalResult"]    
    
    x_train, x_test, y_train , y_test =train_test_split(x,y,test_size=0.5, random_state=42)
      
    model= DecisionTreeClassifier()

    model.fit(x_train, y_train)

    y_pred= model.predict(x_test)

    result= accuracy_score(y_test,y_pred) 

    print(f"accurance scopre: {round(result,2) * 100}")  

    plt.figure(figsize=(12,8))
    plot_tree(model,filled=True,feature_names=feature_col, class_names=[str(x) for x in model.classes_])
    plt.title("ploting students status")
    plt.show()


if __name__=="__main__":
    main()
   