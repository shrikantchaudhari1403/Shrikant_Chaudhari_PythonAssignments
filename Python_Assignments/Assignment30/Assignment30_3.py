import os
import schedule
import time

def printMessage(message):
    print(message)


def main():

     schedule.every(30).minute.do(printMessage="Coding Kar")    

     while True:
          schedule.run_pending()
          time.sleep(1)

 
if __name__ == "__main__":
    main()          