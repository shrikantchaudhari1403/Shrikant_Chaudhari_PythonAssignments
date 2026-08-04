import os
import schedule
import time
import sys

def scanDirectory(directoryName):
    scanDtails=[];
    folderCount = 0
    fileCount = 0
    for folderName, subFolderName, filName in os.walk(directoryName):
        folderCount += len(subFolderName)
        fileCount += len(filName)   

    print(f"Directory scanned : {directoryName}")
    print(f"Total Subdirectories : {folderCount}")
    print(f"Total Files : {fileCount}")
    print(f"Time scanned : {time.ctime()}")
    print("-" * 40)

    for data in scanDtails:
        print(data)       

def main():

     directry= "C:\\Study"

     schedule.every(2).seconds.do(scanDirectory,directry)    

     while True:
          schedule.run_pending()
          time.sleep(1) 


if __name__ == "__main__":
    main()          