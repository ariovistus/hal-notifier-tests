import wpilib
import time
import csv

# I get mean = 180 microseconds, stdev = 300 microseconds


with open('timing.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    start_times = []

    def runnable():
        global start_times
        start = time.time()
        start_times.append(start)

    notifier = wpilib.Notifier(runnable)
    notifier.startPeriodic(0.0001)


    wpilib.Timer.delay(10)
    print ('stop notifier!')
    notifier.stop()
    wpilib.Timer.delay(2)

    for start_time in start_times:
        writer.writerow([start_time])
