import wpilib
import time
import numpy


# I got mean = 400 microseconds, std dev = 33 microseconds
start_times = []

def runnable():
    global start_times
    start = time.time()
    start_times.append(start)

notifier = wpilib.Notifier(runnable)
notifier.startPeriodic(0.0004)


wpilib.Timer.delay(10)
print ('stop notifier!')
notifier.stop()
wpilib.Timer.delay(2)


times = numpy.array(start_times)
time_diffs = times[1:] - times[:-1]

print (time_diffs.mean())
print (time_diffs.std())

