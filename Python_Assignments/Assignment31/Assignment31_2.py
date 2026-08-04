import os
import schedule
import time
import sys

def printMessage(message):
    print(message)


def main():

     message= sys.argv[1]

     schedule.every(5).seconds.do(printMessage,message)    

     while True:
          schedule.run_pending()
          time.sleep(1) 


if __name__ == "__main__":
    main()          