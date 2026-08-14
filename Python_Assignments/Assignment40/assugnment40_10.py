from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd 
from sklearn.metrics import accuracy_score


def main():
    df= pd.read_csv("student_performance_ml.csv")

    features_col= ["StudyHours","PreviousScore"]

    x= df[features_col]
    y= df["FinalResult"]

    print(df.head())

    # radom state 42
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.5,random_state=42)     

    model= DecisionTreeClassifier(random_state=42)
    model.fit(x_train, y_train)
    y_pred= model.predict(x_test)

    result= accuracy_score(y_test,y_pred)

    print(f"accuracy score for random state 42: {round(result,2) *100}")       

    #random state 10 
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.5,random_state=42)   
    model1= DecisionTreeClassifier(max_depth=None)
    model1.fit(x_train,y_train) 
    y_pred = model1.predict(x_test)
    result= accuracy_score(y_test, y_pred)
    print(f"testing accuracy  : {round(result,2) *100}")   
  
    y_pred_train = model1.predict(x_train)
    result= accuracy_score(y_train, y_pred_train)
    print(f"training  accuracy : {round(result,2) *100}")        
      
if __name__=="__main__":
    main()