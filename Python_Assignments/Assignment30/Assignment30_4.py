import datetime
import os
import schedule
import time
import sys

def taskFunction():
    print("Namaskar....")
   
def main():
     schedule.every().day.at("09:00").do(taskFunction)    

     while True:
          schedule.run_pending()
          time.sleep(1)

 
if __name__ == "__main__":
    main()          