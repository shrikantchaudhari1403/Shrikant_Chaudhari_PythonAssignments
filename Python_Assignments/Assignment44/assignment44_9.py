import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({
        'name': ['amit', 'sagar', 'pooja'],
        'math': [85, 90, 78],
        'science': [92, 88, 80],
        'english': [75, 85, 82]
    })

df["Total"] = df[["math", "science", "english"]].sum(axis=1)
