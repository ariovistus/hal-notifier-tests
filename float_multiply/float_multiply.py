import time
import numpy

do_numpy = False

for n in [1,2,5,10,20,40,80, 120, 200, 250, 400, 1000, 10000]:
    x = numpy.array([87*n] * n, dtype='float')
    y = numpy.array([23*n] * n, dtype='float')
    c = numpy.array([0] * n, dtype='float')
    a = time.time()
    if do_numpy:
        numpy.multiply(x, y, out=c)
    else:
        for i in range(n): c = 8723. * 2323.
    b = time.time()
    tm = (b-a) * 1000000
    print ('n: %5s time: %f microseconds' %( n, tm))
