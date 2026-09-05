import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({
        'name': ['amit', 'sagar', 'pooja','ajay'],
        'math': [85, 90, 78,None],
        'science': [None, None, 80,12],
        'english': [75, None, 82,62]
    })

df['math']=df['math'].fillna(df['math'].mean())
df['science']=df['science'].fillna(df['science'].mean())
df['english']=df['english'].fillna(df['english'].mean())
print(df)