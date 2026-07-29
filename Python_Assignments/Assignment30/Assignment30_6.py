import datetime
import os
import schedule
import time
import sys

def lunchTime():
    print("Lunch Time")


def WrapWorkTime():
    print("Wrap The Work")    
   
def main():
     schedule.every().day.at("13:00").do(lunchTime)    
     schedule.every().day.at("18:00").do(WrapWorkTime) 
     
     while True:
          schedule.run_pending()
          time.sleep(1)

 
if __name__ == "__main__":
    main()          