import csv
import wpilib
import numpy

# with moving average taps=1, I get mean=170 microseconds, std dev=9 microseconds
# with moving average taps=4, I get mean=180 microseconds, std dev=12 microseconds
# with moving average taps=40, I get mean=320 microseconds, std dev=16 microseconds
# with moving average taps=400, I get mean=1.7 microseconds, std dev=44 microseconds

# numpy based filter
# with moving average taps=1, I get mean=230 microseconds, std dev=12 microseconds
# with moving average taps=4, I get mean=230 microseconds, std dev=12 microseconds
# with moving average taps=40, I get mean=240 microseconds, std dev=12 microseconds
# with moving average taps=400, I get mean=300 microseconds, std dev=14 microseconds

# collectionless filter
# with moving average taps=1, I get mean=130 microseconds, std dev=8 microseconds
data = []
with open('data.csv', 'r') as f:
    reader = csv.reader(f)

    headers = next(reader)

    for row in reader:
        row = [float(x) for x in row]
        data.append(row)
data = numpy.array(data, dtype='float')

i = 0
def get_datum():
    global i
    if i == 0: 
        i += 1
        return 0
    fps = 50. / 12 * (data[i][1] - data[i-1][1]) / (data[i][0] - data[i-1][0])
    i += 1
    return fps

filter = wpilib.LinearDigitalFilter.movingAverage(get_datum, 1)

ts = data[:, 0]
i = 0
vs2 = [get_datum() for x in data]
i = 1

times = numpy.zeros(shape=(len(data)-1,), dtype='float')
timer = wpilib.Timer()
while i < len(data):
    timer.start()
    filter.pidGet()
    time = timer.get()
    times[i-2] = time


print("mean: ", times.mean())
print("std dev: ", times.std())
