import os

def main():

    path = r"C:\Study\Python\Shrikant_Chaudhari_PythonAssignments\Python_Assignments\Assignment28"

    filenames = input("Enter filenames: ").split()

    fullpath = os.path.join(path, filenames[0])
     
    sourceFile = os.path.join(path, filenames[0])

    destinationFile = os.path.join(path, filenames[1]) 


    try:   
            fobj= open(sourceFile, "r")
            data = fobj.read()          # Read entire file

            fdes= open(destinationFile,"w")
            fdes.write(data)            

    except FileNotFoundError:
        print("Error: File not found!")
        print("Looking for file at:", fullpath)

if __name__ == "__main__":
    main()