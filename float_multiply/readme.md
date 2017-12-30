idle curiosity.

for me, the c version outputs 

```
n:     1, 6.504000 microseconds
n:     2, 5.334000 microseconds
n:     5, 3.729000 microseconds
n:    10, 4.131000 microseconds
n:    20, 4.266000 microseconds
n:    40, 4.539000 microseconds
n:    80, 5.934000 microseconds
n:   120, 7.029000 microseconds
n:   200, 9.543000 microseconds
n:   400, 16.122000 microseconds
n:  1000, 58.986000 microseconds
n: 10000, 343.761000 microseconds
```

the numpy python version outputs

```
n:     1 time: 64.373016 microseconds
n:     2 time: 133.275986 microseconds
n:     5 time: 51.021576 microseconds
n:    10 time: 48.160553 microseconds
n:    20 time: 47.922134 microseconds
n:    40 time: 50.067902 microseconds
n:    80 time: 52.690506 microseconds
n:   120 time: 59.604645 microseconds
n:   200 time: 66.995621 microseconds
n:   250 time: 70.095062 microseconds
n:   400 time: 82.015991 microseconds
n:  1000 time: 148.296356 microseconds
n: 10000 time: 1010.417938 microseconds
```

the non numpy python version outputs
```
n:     1 time: 33.140182 microseconds
n:     2 time: 42.915344 microseconds
n:     5 time: 39.100647 microseconds
n:    10 time: 83.446503 microseconds
n:    20 time: 57.697296 microseconds
n:    40 time: 104.427338 microseconds
n:    80 time: 153.779984 microseconds
n:   120 time: 335.693359 microseconds
n:   200 time: 298.023224 microseconds
n:   250 time: 355.243683 microseconds
n:   400 time: 597.476959 microseconds
n:  1000 time: 1596.450806 microseconds
n: 10000 time: 15689.373016 microseconds
```


bleagh, I'll finish this later
