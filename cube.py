import time

print("type 'stopwatch()' to start")

def timeconvert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

def stopwatch():
    input("Press Enter to start")
    starttime = time.time()
    input("Press Enter to stop")
    endtime = time.time()
    timelapsed = endtime - starttime
    timeconvert(timelapsed)
