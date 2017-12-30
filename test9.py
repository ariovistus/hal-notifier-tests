import wpilib
import time
import numpy


# I get mean = 40 ms, std dev ~ 300 microseconds

start_times = []

def runnable():
    global start_times
    start = time.time()
    start_times.append(start)

notifier = wpilib.Notifier(runnable)
notifier.startPeriodic(0.04)


timer = wpilib.Timer()
timer.start()
while timer.get() < 10:
    numpy.sin(3)
print ('free notifier!')
notifier.free()
wpilib.Timer.delay(2)


times = numpy.array(start_times)
time_diffs = times[1:] - times[:-1]

print (time_diffs.mean())
print (time_diffs.std())

