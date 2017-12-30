import wpilib
import time
import numpy
import csv


# with non-notifier pid controller @ 50 ms, I get mean = 50 ms, std dev ~ 30 microseconds
# with non-notifier pid controller @ 10 ms, I get mean = 10 ms, std dev ~ 24 microseconds
# with non-notifier pid controller @ 1 ms, I get mean = 1 ms, std dev ~ 80 microseconds
# with non-notifier pid controller @ 500 us, I get mean = 511 us, std dev ~ 100 microseconds

# with notifier pid controller @ 50 ms, I get mean = 50 ms, std dev ~ 39 microseconds
# with notifier pid controller @ 10 ms, I get mean = 10 ms, std dev ~ 31 microseconds
# with notifier pid controller @ 1 ms, I get mean = 1 ms, std dev ~ 30 microseconds
# with notifier pid controller @ 500 us, I get mean = 566 us, std dev ~ 20 microseconds
# with notifier pid controller @ 600 us, I get mean = 600 us, std dev ~ 30 microseconds
# with notifier pid controller @ 400 us, I get mean = 566 us, std dev ~ 20 microseconds
# with notifier pid controller @ 580 us, I get mean = 580 us, std dev ~ 43 microseconds
start_times = []

def runnable(result):
    global start_times
    start = time.time()
    if result != 0:
        # ignore the call made by disable
        start_times.append(start)
        #print ('calc! ', start)

pid = wpilib.PIDController(Kp=1, Ki=1, Kd=1, source=lambda: 1, output=runnable, period=0.04)
pid.enable()


wpilib.Timer.delay(10)
tim = time.time()
pid.disable()
wpilib.Timer.delay(2)


times = numpy.array(start_times)
time_diffs = times[1:] - times[:-1]

with open('timing.csv', 'w') as f:
    writer = csv.writer(f)
    for time in start_times:
        writer.writerow([time])

print (time_diffs.mean())
print (time_diffs.std())

