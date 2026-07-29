import os
import schedule
import time

def printMessage(message):
    print(message)


def main():

     schedule.every(2).seconds.do(printMessage,"jay Ganesh")    

     while True:
          schedule.run_pending()
          time.sleep(1) 


 
if __name__ == "__main__":
    main()          