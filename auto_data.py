from ast import literal_eval
from subprocess import run
from requests import get
from sys import exit

def get_date_time():

  url = "http://worldtimeapi.org/api/timezone/America/Manaus"
  response = get(url)
  local_info = literal_eval(str(response.json()))
  time = local_info["datetime"][local_info["datetime"].find("T")+1:19]
  date = local_info["datetime"][:local_info["datetime"].find("T")]

  return date, time

if __name__ == '__main__':
  try:
    date, time = get_date_time()
  except:
    print("Unable to set date and hour")
    exit()
  
  run(["timedatectl", "set-time", date + " " + time])
  print(f'Date and time have been set: {date} {time}')
