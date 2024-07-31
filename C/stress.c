#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

// Don't crash your pc with this one!
// Comments and generated by chatGPT 3.5.
#define MAX_THREADS 100000000  // Maximum number of threads allowed. Be careful with large values!

// Function that threads will run. This function does nothing and loops indefinitely.
void* nothing(void* arg) {
    while (1) {
        // Busy-wait loop. This thread does nothing but will consume CPU time.
    }
    return NULL;  // This line is unreachable due to the infinite loop.
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

    // Create an array of pthread_t to hold thread IDs.
    pthread_t thread[threadcount];

    // Create threads.
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

    // Wait for all threads to finish (they will never finish because of the infinite loop).
    for (int i = 0; i < threadcount; i++) {
        pthread_join(thread[i], NULL);
    }

    // Free the allocated memory.
    free(threads);
    return 0;  // Exit the program successfully.
}
