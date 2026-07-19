import os

def main():

    path = r"C:\Study\Python\Shrikant_Chaudhari_PythonAssignments\Python_Assignments\Assignment28"

    filename = input("Enter filename: ").strip()

    fullpath = os.path.join(path, filename)

    try:   
            fileLines="" 
            fobj= open(fullpath, "r")
            data = fobj.readlines()          # Read entire file
            for lines in data:
                fileLines+=lines 

            print(f"file", fileLines)

    except FileNotFoundError:
        print("Error: File not found!")
        print("Looking for file at:", fullpath)

if __name__ == "__main__":
    main()