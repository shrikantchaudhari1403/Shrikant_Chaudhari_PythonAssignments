from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def main():
      df= pd.DataFrame({
              'name': ['amit', 'sagar','pooja'],
              'math':[85,90,78],
              'science':[92,88,80],
              'english':[75,85,82]
         }) 
      scaler = MinMaxScaler()

      df['gender']=["male","male","fimale"]

      df= pd.get_dummies(df,columns=['gender'], dtype=int)

      print(df)
   
if __name__=="__main__":
    main()