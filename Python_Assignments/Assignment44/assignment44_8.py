import pandas as pd
import matplotlib.pyplot as plt

def main():

    df = pd.DataFrame({
        'name': ['amit', 'sagar', 'pooja'],
        'math': [85, 90, 78],
        'science': [92, 88, 80],
        'english': [75, 85, 82]
    })

    df["Total"] = df[["math", "science", "english"]].sum(axis=1)

    # Get Amit's row
    amit = df[df["name"] == "amit"].iloc[0]

    subjects = ["math", "science", "english"]
    marks = [amit["math"], amit["science"], amit["english"]]

    plt.figure(figsize=(8, 5))

    plt.plot(subjects, marks, marker="o", label="Amit")

    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Amit's Marks Across Subjects")
    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()