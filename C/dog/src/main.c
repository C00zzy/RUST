#include <stdio.h>

int main(void)
{
    int human;
    long result;

    printf("What is your age?\n");
    scanf("%d", &human);
    result = (long)human * 7;
    printf("%ld\n", result);
}