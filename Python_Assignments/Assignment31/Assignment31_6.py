import os
import schedule
import time
import sys

def printMessage(message):
    print(message)

def main():
     
     schedule.every().monday.at("09:00").do(printMessage,"Monday at 9:00 AM :Start your weekly goals")
     schedule.every().wednesday.at("17:00").do(printMessage,"Wednesday at  5 pm : Review your weekly progress")   
     schedule.every().friday.at("18:00").do(printMessage,"Firday at 6 pm:  Weekly work completed")   
    
     while True:
          schedule.run_pending()
          time.sleep(1) 

if __name__ == "__main__":
    main()          