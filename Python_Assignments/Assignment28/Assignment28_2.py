import os

def main():

    path = r"C:\Study\Python\Shrikant_Chaudhari_PythonAssignments\Python_Assignments\Assignment28"

    filename = input("Enter filename: ").strip()

    fullpath = os.path.join(path, filename)

    try:
            fobj= open(fullpath, "r")
            data = fobj.read()          # Read entire file
            words = data.split()        # Split into words
            count = len(words)          # Count words

            print(f"Total number of words in '{filename}' is {count}")

    except FileNotFoundError:
        print("Error: File not found!")
        print("Looking for file at:", fullpath)

if __name__ == "__main__":
    main()