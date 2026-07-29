import datetime
import os
import schedule
import time
import sys
import shutil


def WrapWorkTime():
    print("Wrap The Work")    
   
def main():
    
     sourceFile= sys.argv[1]
     ret= os.path.isfile(sys.argv[1])

     if ret == False:
         return

     destinationFolder= sys.argv[2]

     ret= os.path.isdir(destinationFolder)

     if ret == False:
        os.mkdir(destinationFolder)

     
     timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
     fileName= os.path.join(destinationFolder, "Data_%s.log" %timeStamp)

     shutil.copy(sourceFile, fileName)

if __name__ == "__main__":
    main()          