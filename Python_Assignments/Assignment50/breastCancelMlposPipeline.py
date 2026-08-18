import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as pn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


# step 1: load the data
# description: it load the data from data source
# input : source scv
# output : dataframe
# author : shrikant chaudhari
def loadData(fileName):
    df= pd.read_csv(fileName)
    return df


# step preProcess: pre process the csv
# description: it pre process the csv
# input : dataframe
# output : dataframe
# author : shrikant chaudhari
def preProcessData(df: pd.DataFrame):

    # Drop ID column
    df = df.drop(columns="CodeNumber")

    features = [
        "ClumpThickness",
        "UniformityCellSize",
        "UniformityCellShape",
        "MarginalAdhesion",
        "SingleEpithelialCellSize",
        "BareNuclei",
        "BlandChromatin",
        "NormalNucleoli",
        "Mitoses"
    ]

    # Convert all feature columns to numeric
    # Invalid values such as '?' become NaN
    for column in features:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # Fill missing values with median
    for column in features:
        df[column] = df[column].fillna(
            df[column].median()
        )

    return df

# step split: split the data for testing and training 
# description: it split the data
# input : dataframe
# output : X_train, X_test, Y_train , Y_test 
# author : shrikant chaudhari
def splitData(df: pd.DataFrame):
    features= ["ClumpThickness","UniformityCellSize","UniformityCellShape","MarginalAdhesion","SingleEpithelialCellSize","BareNuclei","BlandChromatin","NormalNucleoli","Mitoses"]

    X = df[features]
    Y = df["CancerType"]

    X_train, X_test, Y_train, Y_test= train_test_split(X,Y, test_size=0.2, random_state=42)
    return X_train, X_test, Y_train,Y_test 
   

# step train model: train te model
# description:trainModel - it trains the model
# input : dataframe
# output : X_train, X_test, Y_train , Y_test 
# author : shrikant chaudhari
def trainModel(model:LogisticRegression,X_train,Y_train):
    model= model.fit(X_train,Y_train)
    return model     

# step Evaluate the model
# description:evaluateModel - it evaluates the model
# input : model, X_test, Y_test
# output :node
# author : shrikant chaudhari
def evaluateModel(model:LogisticRegression, X_test, Y_test):
    Y_pred= model.predict(X_test)
    result= accuracy_score(Y_test,Y_pred)
    print(confusion_matrix(Y_test,Y_pred))
    print("Accuracy score is :", round(result*100,2))

# step main: main entry program
# description: it calls all other process pipelines
# input : none
# output : none
# author : shrikant chaudhari
def main():
    # step1 load csv
    df= loadData("breast-cancer-wisconsin.csv")
    # step 2 preprocess the file 
    df= preProcessData(df)
    # step 3 split data set
    X_train, X_test, Y_train, Y_test = splitData(df) 
    # step 4 train the model
    model = LogisticRegression(max_iter=1000)
    model= trainModel(model, X_train,Y_train)
    # step 5 Evaluate the model
    evaluateModel(model,X_test,Y_test)

if __name__=="__main__":
    main()
