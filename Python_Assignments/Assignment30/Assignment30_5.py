import datetime
import os
import schedule
import time
import sys

def write_to_file():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fobj= open("Marvellous.txt","a")
    fobj.write(current_time+"\n")
    fobj.close() 
   
def main():
     schedule.every(5).minute.do(write_to_file)    

     while True:
          schedule.run_pending()
          time.sleep(1)

 
if __name__ == "__main__":
    main()          