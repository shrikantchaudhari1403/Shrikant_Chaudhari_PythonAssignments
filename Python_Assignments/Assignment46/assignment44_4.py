import pandas as pd
import numpy as nump

def main():
    data= [{'name': ['amit', 'sagar','pooja'],
          'math':[85,90,78],
          'science':[92,88,80],
          'english':[75,85,82]
        }]

    df= pd.DataFrame({
          'name': ['amit', 'sagar','pooja'],
          'math':[85,90,78],
          'science':[92,88,80],
          'english':[75,85,82]
     })  


   # print(df.describe())
    
   # df["Total"] =sum(df['math']) +sum(df['science']) + sum(df['english'])
    df["Total"] = df[["math", "science", "english"]].sum(axis=1)
   # print(df)
   # students scored more than 85 in science

    result= df[df["science"] > 85]

    print(result)

if __name__=="__main__":
    main()