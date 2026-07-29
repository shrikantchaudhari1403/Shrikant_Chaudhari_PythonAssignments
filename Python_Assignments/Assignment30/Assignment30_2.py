import os
import schedule
import time

def printMessage():
    print(time.ctime())


def main():

     schedule.every(1).minute.do(printMessage)    

     while True:
          schedule.run_pending()
          time.sleep(40)

 
if __name__ == "__main__":
    main()          