#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>

#define MAX_THREADS 1000
#define NUM_CPU_FIELDS 10

void* nothing(void* arg) {
	volatile long long int counter = 0;
    while (1) {
	    counter++;
    }
    return NULL;  // This line is unreachable due to the infinite loop.
}

void get_cpu_times(long *cpu_times) {
    FILE *file = fopen("/proc/stat", "r");
    if (!file) {
        perror("Failed to open file...");
        exit(EXIT_FAILURE);
    }
    fscanf(file, "cpu %ld %ld %ld %ld %ld %ld %ld %ld %ld %ld",
           &cpu_times[0], &cpu_times[1], &cpu_times[2], &cpu_times[3],
           &cpu_times[4], &cpu_times[5], &cpu_times[6], &cpu_times[7],
           &cpu_times[8], &cpu_times[9]);
    fclose(file);
}

double cpu_usage_calculation(long *prev_times, long *curr_times) {
    long prev_idle = prev_times[3];
    long curr_idle = curr_times[3];

    long prev_total = 0;
    long curr_total = 0;
    for (int i = 0; i < NUM_CPU_FIELDS; i++) {
        prev_total += prev_times[i];
        curr_total += curr_times[i];
    }

    long total_diff = curr_total - prev_total;
    long idle_diff = curr_idle - prev_idle;

    if (total_diff == 0) return 0.0; // Prevent division by zero

    double cpu_usage = (total_diff - idle_diff) * 100.0 / total_diff;
    return cpu_usage;
}

void handle_signal(int signal) {
    printf("Exit signal detected!\n");
    exit(0);
}

int main() {
    int threadcount;
    printf("How many threads?\n");
    printf("If needed you can time this application with the time application on linux\n");
    scanf("%d", &threadcount);

    if (threadcount < 0 || threadcount > MAX_THREADS) {
        printf("Invalid thread count!\n");
        exit(EXIT_FAILURE);
    }

    pthread_t threads[threadcount];
    for (int i = 0; i < threadcount; i++) {
        if (pthread_create(&threads[i], NULL, nothing, NULL) != 0) {
            perror("pthread_create");
            exit(EXIT_FAILURE);
        }
    }
    printf("Stressing %d threads\n", threadcount);

    if (signal(SIGINT, handle_signal) == SIG_ERR || signal(SIGTERM, handle_signal) == SIG_ERR) {
        perror("Error setting up signal handlers");
        exit(EXIT_FAILURE);
    }

    while (1) {
        long prev_times[NUM_CPU_FIELDS];
        long curr_times[NUM_CPU_FIELDS];

        get_cpu_times(prev_times);
        sleep(1);
        get_cpu_times(curr_times);

        double cpu_usage = cpu_usage_calculation(prev_times, curr_times);
        printf("CPU Usage: %.2f%%\n", cpu_usage);
    }

    for (int i = 0; i < threadcount; i++) {
        pthread_cancel(threads[i]); // Cancel the threads gracefully
    }
    return 0;
}

