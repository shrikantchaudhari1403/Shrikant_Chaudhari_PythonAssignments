import os

def main():

    path = r"C:\Study\Python\Shrikant_Chaudhari_PythonAssignments\Python_Assignments\Assignment28"

    filenameWord = input("Enter filename and word: ").split()


    filename = os.path.join(path, filenameWord[0])

    searchWord= filenameWord[1]

    try:   
            fobj= open(filename, "r")
            data = fobj.read()         # Read entire file
            
            if searchWord in data.split():
               print(f"'{searchWord}' is present in the file.")
            else:
               print(f"'{searchWord}' is NOT present in the file.")

    except FileNotFoundError:
        print("Error: File not found!")

if __name__ == "__main__":
    main()