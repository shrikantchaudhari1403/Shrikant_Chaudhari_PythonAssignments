import pandas as pd

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


    print(df.describe())
    
   
if __name__=="__main__":
    main()