import os
import sys

def main():
    fullpath="C:\\Study\\Python\\Shrikant_Chaudhari_PythonAssignments\\Python_Assignments\\Assignment29"
    fileName= sys.argv[1]
    fileRead= os.path.join(fullpath,fileName)
    if os.path.isfile(fileRead):
       data=open(fileRead,"r")
       content = data.read()
       fobj= open(os.path.join(fullpath,"copy.txt"),"w")
       fobj.write(content)
    else:
        print("file not exists")
if __name__=="__main__":
    main()