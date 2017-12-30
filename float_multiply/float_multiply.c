#include <time.h>
#include <stdio.h>


// call this function to start a nanosecond-resolution timer
struct timespec timer_start(){
    struct timespec start_time;
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &start_time);
    return start_time;
}

// call this function to end a timer, returning nanoseconds elapsed as a long
long timer_end(struct timespec start_time){
    struct timespec end_time;
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &end_time);
    long diffInNanos = end_time.tv_nsec - start_time.tv_nsec;
    return diffInNanos;
}

int main() {
    int times[] = {
        1, 2, 5, 10, 20,
        40, 80, 120, 200,
        400, 1000, 10000
    };
    for(int in = 0; in < 12; in++) {
        int n = times[in];
        float f1 = 8723 * in, f2 = 2323 * in;
        struct timespec t = timer_start();
        float c = 0;

        for(int i = 0; i < n; i++) {
            c += f1 * f2;
        }

        double seconds = timer_end(t) / 1000.;

        printf("n: %5d, %f microseconds %f\n", n, seconds, c /* stupid optimizer */);
    }
}
