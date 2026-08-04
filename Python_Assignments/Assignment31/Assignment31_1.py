import os
import schedule
import time
import sys

def printMessage(message):
    print(message)


def main():

     message= sys.argv[1]
     timeInterval=int(sys.argv[2])

     schedule.every(timeInterval).seconds.do(printMessage,message)    

     while True:
          schedule.run_pending()
          time.sleep(1) 


if __name__ == "__main__":
    main()          