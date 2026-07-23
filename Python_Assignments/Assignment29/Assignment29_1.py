import os

def checkFileExists(name):
    fullpath="C:\Study\Python\Shrikant_Chaudhari_PythonAssignments\Python_Assignments\Assignment29"
    
    path= os.path.join(fullpath,name);
    return os.path.isfile(path)

def main():

    fileTxt = input("Enter filename: ")
  
    if checkFileExists(fileTxt):
        print("File exists")
    else:
        print("File does not exist")

if __name__ == "__main__":
    main()