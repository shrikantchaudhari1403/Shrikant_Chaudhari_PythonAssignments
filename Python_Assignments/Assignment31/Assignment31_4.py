import os
import schedule
import time
import sys

def printMessage():
    timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    fobj= open("MarvellousLog_%s" %timeStamp,"w")

    fobj.write("Log file create successfully \n")
    fobj.write(f"Creation time: {timeStamp}")
    fobj.close()

def main():
     schedule.every(10).minutes.do(printMessage)    

     while True:
          schedule.run_pending()
          time.sleep(1) 

if __name__ == "__main__":
    main()          