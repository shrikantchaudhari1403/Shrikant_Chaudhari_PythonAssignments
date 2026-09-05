import pandas as pd

def main():
      df= pd.DataFrame({
              'name': ['amit', 'sagar','pooja'],
              'math':[85,90,78],
              'science':[92,88,80],
              'english':[75,85,82]
         }) 

      df['gender']=["male","male","fimale"]

      avgMarks= df.groupby('gender')['name','math','science','english']
      print(avgMarks)
   
if __name__=="__main__":
    main()