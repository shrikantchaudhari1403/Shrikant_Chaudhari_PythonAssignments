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

    df["Total"] = df[["math", "science", "english"]].sum(axis=1)

    
    df= df.sort_values("Total",ascending=False)

    print(df)
    
if __name__=="__main__":
    main()