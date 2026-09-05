import pandas as pd
import numpy as nump
import matplotlib.pyplot as plt

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

    plt.figure(figsize=(12,8)) 
    
    plt.bar(df["name"], df["Total"], edgecolor='blue', label="Total Marks")

    plt.xlabel("Student Name")

    plt.ylabel("Marks")

    plt.legend()

    plt.show()
       

if __name__=="__main__":
    main()