import wpilib
import time
import numpy
import csv


# at period 40 ms, I get mean = 40 ms, std dev ~ 300 microseconds
# at period 5 ms, I get mean = 5 ms, std dev ~ 280 microseconds
# at period 1 ms, I get mean = 1 ms, std dev ~ 800 microseconds

start_times = []

def runnable():
    global start_times
    start = time.time()
    start_times.append(start)

notifier = wpilib.Notifier(runnable)
notifier.startPeriodic(0.001)


timer = wpilib.Timer()
timer.start()
while timer.get() < 10:
    numpy.sin(3)
print ('free notifier!')
notifier.free()
wpilib.Timer.delay(2)


times = numpy.array(start_times)
time_diffs = times[1:] - times[:-1]

with open('timing.csv', 'w') as f:
    writer = csv.writer(f)
    for time in start_times:
        writer.writerow([time])

print (time_diffs.mean())
print (time_diffs.std())

