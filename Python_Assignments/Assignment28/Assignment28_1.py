import os

def main():

    path = r"C:\Study\Python\Shrikant_Chaudhari_PythonAssignments\Python_Assignments\Assignment28"

    filename = input("Enter filename: ").strip()

    fullpath = os.path.join(path, filename)

    try:
            fobj= open(fullpath, "r")
            count = len(fobj.readlines())

            print(f"Total number of lines in '{filename}' is {count}")

    except FileNotFoundError:
        print("Error: File not found!")
        print("Looking for file at:", fullpath)

if __name__ == "__main__":
    main()