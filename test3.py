import wpilib
import time
import csv

# I get mean = 20 ms, stdev = 24 microseconds

with open('timing.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    start_times = [0.0] * 500
    i = 0

    def runnable():
        global start_times, i
        start = time.time()
        timer = wpilib.Timer()
        timer.start()
        while timer.get() < 0.00002:
            pass
        start_times[i] = start
        i+=1
    notifier = wpilib.Notifier(runnable)

    notifier.startPeriodic(0.02)


    wpilib.Timer.delay(10)
    print ('stop notifier!')
    notifier.stop()
    wpilib.Timer.delay(2)

    for start_time in start_times:
        writer.writerow([start_time])
