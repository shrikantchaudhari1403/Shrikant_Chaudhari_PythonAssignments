import os
import sys

def openFileContent(filName, worldName):
     fullpath="C:\\Study\\Python\\Shrikant_Chaudhari_PythonAssignments\\Python_Assignments\\Assignment29"
     path = os.path.join(fullpath,filName);
     if os.path.isfile(path):    
        content= open(path,"r")
        data= content.readlines()
        count =0
        for line in data:
                arrline= line.split()
                for worl in arrline:
                    if worl == worldName:
                         count= count+1     

                    continue   

        print("given world occures :", str(count) +" times")                
     else:
         print("file not found")   


def main():
    openFileContent(sys.argv[1], sys.argv[2])

if __name__== "__main__":
    main()