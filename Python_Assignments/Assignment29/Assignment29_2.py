import os

def openFileContent(filName):
     fullpath="C:\Study\Python\Shrikant_Chaudhari_PythonAssignments\Python_Assignments\Assignment29"
     path = os.path.join(fullpath,filName);
     if os.path.isfile(path):    
        content= open(path,"r")
        data= content.read()
        print(data)
     else:
         print("file not found")   
def main():
    fileName= input("Enter file name :")
    openFileContent(fileName)

if __name__== "__main__":
    main()