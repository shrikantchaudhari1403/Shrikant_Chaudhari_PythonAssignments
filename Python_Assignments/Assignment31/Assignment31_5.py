import os
import schedule
import time
import sys

def scanDirectory(directry):
    fileCount = 0
    timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    fobj= open("log/DirectoryCountingLig.txt","+a")
    for directoryName,subDirectoryName,fileNames in os.walk(directry):
        for files in fileNames:
            fileCount+= len(files) 

    fobj.write(" path:" "log/DirectoryCountingLig.txt \n")    
    fobj.write(f"file Count :  {fileCount} \n") 
    fobj.write(f" date & Time :  {timeStamp} \n") 
    fobj.close()
    

def main():
    
     directry= "C:\\Study"
     schedule.every(5).seconds.do(scanDirectory,directry)       

     while True:
          schedule.run_pending()
          time.sleep(1) 

if __name__ == "__main__":
   
    main()          