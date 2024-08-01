#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>

// Define the maximum number of threads allowed. Be cautious with very high values.
#define MAX_THREADS 100000000  

// Define the number of fields in the /proc/stat file related to CPU times.
#define NUM_CPU_FIELDS 10

// Function that threads will run. This function does nothing and loops indefinitely.
void* nothing(void* arg) {
    while (1) {
        // Busy-wait loop. This thread does nothing but will consume CPU time.
    }
    return NULL;  // This line is unreachable due to the infinite loop.
}

// Function to read CPU times from /proc/stat and store them in the provided array.
void get_cpu_times(long *cpu_times) {
    FILE *file = fopen("/proc/stat", "r");
    if (!file) {
        perror("Failed to open file...\n");
        exit(EXIT_FAILURE);
    }
    // Read the CPU times from the file.
    fscanf(file, "cpu %ld %ld %ld %ld %ld %ld %ld %ld %ld %ld",
           &cpu_times[0], &cpu_times[1], &cpu_times[2], &cpu_times[3],
           &cpu_times[4], &cpu_times[5], &cpu_times[6], &cpu_times[7],
           &cpu_times[8], &cpu_times[9]);
    fclose(file);
}

// Function to calculate CPU usage percentage based on previous and current CPU times.
double cpu_usage_calculation(long *prev_times, long *curr_times) {
    // Calculate the difference in idle times.
    long prev_idle = prev_times[3];
    long curr_idle = curr_times[3];

    // Calculate the difference in total times.
    long prev_total = 0;
    long curr_total = 0;
    for (int i = 0; i < NUM_CPU_FIELDS; i++) {
        prev_total += prev_times[i];
        curr_total += curr_times[i];
    }

    long total_diff = curr_total - prev_total;
    long idle_diff = curr_idle - prev_idle;

    // Calculate CPU usage percentage.
    double cpu_usage = (total_diff - idle_diff) * 100.0 / total_diff;
    return cpu_usage;
}

// Signal handler function for detecting exit signals (SIGINT, SIGTERM).
void handle_signal(int signal) {
    printf("Exit signal detected!\n");
    exit(0);
}

int main() {
    int threadcount;
    // Prompt the user to enter the number of threads to create.
    printf("How many threads?\n");
    printf("If needed you can time this application with the time application on linux\n");
    scanf("%d", &threadcount);  // Read the number of threads from standard input.

    // Check if the entered thread count is valid.
    if (threadcount < 0 || threadcount > MAX_THREADS) {
        printf("Invalid thread count!\n");  // Print an error message if the count is invalid.
        exit(EXIT_FAILURE);  // Exit the program with a failure status.
    }

    // Allocate memory for an array of pthread_t structures.
    pthread_t* threads = (pthread_t*)malloc(threadcount * sizeof(pthread_t));
    if (threads == NULL) {
        perror("malloc");  // Print an error message if memory allocation fails.
        exit(EXIT_FAILURE);  // Exit the program with a failure status.
    }

    // Set up signal handlers for SIGINT (Ctrl+C) and SIGTERM (kill).
    if (signal(SIGINT, handle_signal) == SIG_ERR) {
        perror("Exiting!\n");
        free(threads);
        exit(EXIT_FAILURE);
    }

    if (signal(SIGTERM, handle_signal) == SIG_ERR) {
        perror("Exiting!\n");
        free(threads);
        exit(EXIT_FAILURE);
    }

    // Create threads.
    pthread_t thread[threadcount];
    for (int i = 0; i < threadcount; i++) {
        // Start a new thread running the 'nothing' function.
        if (pthread_create(&thread[i], NULL, nothing, NULL) != 0) {
            perror("pthread_create");  // Print an error message if thread creation fails.
            free(threads);  // Free allocated memory before exiting.
            exit(EXIT_FAILURE);  // Exit the program with a failure status.
        }
    }
    // Inform the user that threads are being created.
    printf("Stressing %d threads\n", threadcount);

    // Loop to continuously measure and display CPU usage.
    while (1) {
        long prev_times[NUM_CPU_FIELDS];
        long curr_times[NUM_CPU_FIELDS];

        // Get CPU times before and after sleeping for 1 second.
        get_cpu_times(prev_times);
        sleep(1);
        get_cpu_times(curr_times);

        // Calculate and print the CPU usage percentage.
        double cpu_usage = cpu_usage_calculation(prev_times, curr_times);
        printf("CPU Usage: %.2f%%\n", cpu_usage);
    }

    // Wait for all threads to finish (they will never finish due to the infinite loop).
    for (int i = 0; i < threadcount; i++) {
        pthread_join(thread[i], NULL);
    }

    // Free the allocated memory.
    free(threads);
    return 0;  // Exit the program successfully.
}
