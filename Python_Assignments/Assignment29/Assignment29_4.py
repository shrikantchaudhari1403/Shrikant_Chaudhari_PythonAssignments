import os
import sys

def openFileContent(sourceName,targetName):
     fullpath="C:\\Study\\Python\\Shrikant_Chaudhari_PythonAssignments\\Python_Assignments\\Assignment29"
     
     sourcePath = os.path.join(fullpath, sourceName)
     targetPath = os.path.join(fullpath, targetName)

     if os.path.isfile(sourcePath):    
        content= open(sourcePath,"r")
        fobj= open(targetPath,"w")
        data= content.read()
        fobj.write(data)
        content.close()
        fobj.close()
     else:
         print("file not found")   
def main():
   # fileName= input("Enter file names :")
    openFileContent(sys.argv[1], sys.argv[2])

if __name__== "__main__":
    main()