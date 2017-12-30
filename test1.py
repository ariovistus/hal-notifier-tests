import wpilib
import time
import csv

# I get mean = 20 ms, stdev = 30 microseconds

with open('timing.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)

    def runnable():
        global writer
        start = time.time()
        print ('called runnable at ', start)
        print ('begin wait 20 us')
        timer = wpilib.Timer()
        timer.start()
        while timer.get() < 0.00002:
            pass
        print ('end wait 20 us')
        end = time.time()
        print ('finished runnable at ', end)
        writer.writerow([start, end])
    notifier = wpilib.Notifier(runnable)

    notifier.startPeriodic(0.02)


    wpilib.Timer.delay(10)
    print ('stop notifier!')
    notifier.stop()
    wpilib.Timer.delay(2)
